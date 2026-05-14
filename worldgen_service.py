# ============================================================================
# WORLDGEN SERVICE — Python Flask Wrapper for WorldGen
# ============================================================================
# server/worldgen_service.py
# Provides REST API and WebSocket endpoints for Synth OS integration
# Requires: pip install worldgen (from https://github.com/ZiYang-xie/WorldGen)

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import torch
from PIL import Image
import os
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for Synth OS frontend
socketio = SocketIO(app, cors_allowed_origins="*")

# ============================================================================
# 1. WORLDGEN INITIALIZATION
# ============================================================================

# Initialize WorldGen (lazy loading to handle import errors gracefully)
worldgen = None
device = None

def init_worldgen():
    global worldgen, device
    try:
        from worldgen import WorldGen
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        worldgen = WorldGen(mode="t2s", device=device, low_vram=False)
        logger.info(f"WorldGen initialized on {device}")
    except ImportError:
        logger.warning("WorldGen not installed. Running in mock mode.")
        worldgen = None

# Initialize on first request
@app.before_request
def before_request():
    if worldgen is None and device is None:
        init_worldgen()

# ============================================================================
# 2. IN-MEMORY STORAGE
# ============================================================================

# Store generated worlds
worlds_db: Dict[str, Dict[str, Any]] = {}

# Store active explorations (Viser instances)
active_explorations: Dict[str, Any] = {}

# ============================================================================
# 3. API ENDPOINTS
# ============================================================================

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'worldgen_loaded': worldgen is not None,
        'device': str(device) if device else 'none',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/generate', methods=['POST'])
def generate_scene():
    data = request.json
    prompt = data.get('prompt', 'A beautiful landscape with mountains and rivers')
    return_mesh = data.get('return_mesh', False)
    mode = data.get('mode', 't2s')
    resolution = data.get('resolution', 'high')
    agent_id = data.get('agent_id', 'unknown')
    generation = data.get('generation', 0)

    logger.info(f"Generating world for agent {agent_id}, generation {generation}")
    logger.info(f"Prompt: {prompt[:100]}...")

    try:
        if worldgen is None:
            # Mock mode: return placeholder
            world_id = hashlib.md5(prompt.encode()).hexdigest()
            output_path = f"output/mock_{world_id}.ply"

            worlds_db[world_id] = {
                'id': world_id,
                'prompt': prompt,
                'output_path': output_path,
                'agent_id': agent_id,
                'generation': generation,
                'created_at': datetime.now().isoformat(),
                'mock': True
            }

            return jsonify({
                'status': 'success',
                'output_path': output_path,
                'mesh_path': None,
                'navmesh': True,
                'walkable_surface': 0.75,
                'world_id': world_id,
                'mock': True
            })

        # Real WorldGen generation
        if mode == 'i2s' and 'image' in data:
            image = Image.open(data['image'])
            splat = worldgen.generate_world(
                image=image,
                prompt=prompt
            )
        else:
            splat = worldgen.generate_world(prompt)

        world_id = hashlib.md5(f"{prompt}-{agent_id}-{generation}".encode()).hexdigest()
        output_dir = f"output/{agent_id}"
        os.makedirs(output_dir, exist_ok=True)

        output_path = f"{output_dir}/{world_id}.ply"
        splat.save(output_path)

        mesh_path = None
        if return_mesh:
            mesh = worldgen.generate_world(prompt, return_mesh=True)
            mesh_path = f"{output_dir}/{world_id}_mesh.ply"
            import open3d as o3d
            o3d.io.write_triangle_mesh(mesh_path, mesh)

        # Store world metadata
        worlds_db[world_id] = {
            'id': world_id,
            'prompt': prompt,
            'output_path': output_path,
            'mesh_path': mesh_path,
            'agent_id': agent_id,
            'generation': generation,
            'created_at': datetime.now().isoformat(),
            'mock': False
        }

        return jsonify({
            'status': 'success',
            'output_path': output_path,
            'mesh_path': mesh_path,
            'navmesh': True,
            'walkable_surface': 0.75,
            'world_id': world_id,
            'mock': False
        })

    except Exception as e:
        logger.error(f"Generation error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/explore', methods=['GET'])
def launch_explorer():
    world_id = request.args.get('scene')

    if not world_id or world_id not in worlds_db:
        return jsonify({
            'status': 'error',
            'message': 'World not found'
        }), 404

    world = worlds_db[world_id]

    try:
        # Launch Viser server for real-time exploration
        # Note: This requires viser to be installed
        # pip install git+https://github.com/ZiYang-xie/viser.git

        import subprocess
        import threading

        def start_viser():
            port = 8080 + len(active_explorations)
            cmd = [
                'python', '-m', 'viser.server',
                '--scene', world['output_path'],
                '--port', str(port)
            ]
            process = subprocess.Popen(cmd)
            active_explorations[world_id] = {
                'process': process,
                'port': port,
                'url': f'http://localhost:{port}'
            }

        thread = threading.Thread(target=start_viser)
        thread.start()

        # Wait a moment for server to start
        import time
        time.sleep(2)

        exploration = active_explorations.get(world_id)
        if exploration:
            return jsonify({
                'status': 'exploring',
                'url': exploration['url'],
                'world_id': world_id
            })
        else:
            # Fallback: return file path for direct loading
            return jsonify({
                'status': 'file_ready',
                'file_path': world['output_path'],
                'world_id': world_id
            })

    except Exception as e:
        logger.error(f"Exploration error: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/world/<world_id>', methods=['GET'])
def get_world(world_id):
    if world_id not in worlds_db:
        return jsonify({
            'status': 'error',
            'message': 'World not found'
        }), 404

    return jsonify({
        'status': 'success',
        'world': worlds_db[world_id]
    })

@app.route('/world/<world_id>', methods=['DELETE'])
def delete_world(world_id):
    if world_id not in worlds_db:
        return jsonify({
            'status': 'error',
            'message': 'World not found'
        }), 404

    world = worlds_db.pop(world_id)

    # Clean up files
    try:
        if os.path.exists(world['output_path']):
            os.remove(world['output_path'])
        if world.get('mesh_path') and os.path.exists(world['mesh_path']):
            os.remove(world['mesh_path'])
    except Exception as e:
        logger.warning(f"Cleanup error: {str(e)}")

    return jsonify({
        'status': 'success',
        'message': 'World deleted'
    })

@app.route('/update', methods=['POST'])
def update_world():
    data = request.json
    world_id = data.get('worldId')
    actions = data.get('actions', [])

    if not world_id or world_id not in worlds_db:
        return jsonify({
            'status': 'error',
            'message': 'World not found'
        }), 404

    world = worlds_db[world_id]

    # Process agent actions
    # In a full implementation, this would modify the Gaussian Splat
    # For now, we record the actions and emit updates

    update_event = {
        'worldId': world_id,
        'type': 'agent-action',
        'data': {
            'actions': actions,
            'timestamp': datetime.now().isoformat()
        },
        'timestamp': datetime.now().isoformat()
    }

    # Emit to all connected clients watching this world
    socketio.emit(f'world-{world_id}', update_event)

    return jsonify({
        'status': 'success',
        'world': world,
        'update': update_event
    })

@app.route('/worlds', methods=['GET'])
def list_worlds():
    agent_id = request.args.get('agent_id')

    worlds = list(worlds_db.values())
    if agent_id:
        worlds = [w for w in worlds if w.get('agent_id') == agent_id]

    return jsonify({
        'status': 'success',
        'worlds': worlds,
        'count': len(worlds)
    })

# ============================================================================
# 4. WEBSOCKET EVENTS
# ============================================================================

@socketio.on('connect')
def handle_connect():
    logger.info(f"Client connected: {request.sid}")
    emit('connected', {'status': 'connected', 'sid': request.sid})

@socketio.on('disconnect')
def handle_disconnect():
    logger.info(f"Client disconnected: {request.sid}")

@socketio.on('join-world')
def handle_join_world(data):
    world_id = data.get('worldId')
    agent_id = data.get('agentId')

    if world_id in worlds_db:
        # Join room for this world
        from flask_socketio import join_room
        join_room(world_id)

        emit('world-joined', {
            'worldId': world_id,
            'agentId': agent_id,
            'world': worlds_db[world_id]
        })

        # Notify other agents in this world
        emit('agent-joined', {
            'agentId': agent_id,
            'timestamp': datetime.now().isoformat()
        }, room=world_id, include_self=False)
    else:
        emit('error', {'message': 'World not found'})

@socketio.on('agent-action')
def handle_agent_action(data):
    world_id = data.get('worldId')
    action = data.get('action')

    if world_id in worlds_db:
        # Broadcast action to all agents in world
        emit('agent-action', {
            'worldId': world_id,
            'action': action,
            'timestamp': datetime.now().isoformat()
        }, room=world_id)

@socketio.on('world-morph')
def handle_world_morph(data):
    world_id = data.get('worldId')
    morph_data = data.get('morphData')

    if world_id in worlds_db:
        # Trigger world regeneration with new parameters
        emit('world-morphing', {
            'worldId': world_id,
            'morphData': morph_data,
            'timestamp': datetime.now().isoformat()
        }, room=world_id)

# ============================================================================
# 5. MAIN
# ============================================================================

if __name__ == '__main__':
    # Create output directory
    os.makedirs('output', exist_ok=True)

    # Initialize WorldGen
    init_worldgen()

    # Start server
    logger.info("Starting WorldGen Service on port 5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
