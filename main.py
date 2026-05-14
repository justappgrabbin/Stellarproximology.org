import os
from flask import Flask, request, jsonify, render_template_string, render_template
from universe_builder.builder_engine import UniverseBuilder
from cynthia import Cynthia
from spec1_calculator import calculate_gate_line_color_tone_base
from memory_hub.trigger_index import load_module_from_keyword
from gate_codon_mapper import CompleteGateCodonMapper, generate_enhanced_sentence_with_biological_context

app = Flask(__name__)

UPLOAD_DIR = "uploads"
GENERATED_DIR = "generated_app"
LOG_DIR = "logs"

# Ensure folders exist
for folder in [UPLOAD_DIR, GENERATED_DIR, LOG_DIR]:
    os.makedirs(folder, exist_ok=True)

# Initialize Cynthia
cynthia = Cynthia()

# Initialize Memory Snatcher
from memory_snatcher import start_memory_snatcher
memory_snatcher = start_memory_snatcher(cynthia_instance=cynthia)

# Initialize Gate→Codon→Element mapper
gate_mapper = CompleteGateCodonMapper()

# Initialize mobile API components
from components.mobile_api import MobileAPI
mobile_api = MobileAPI(app, cynthia)

# Initialize Field Incubation Engine
from field_incubation_engine import FieldIncubationEngine
from lab_logic import lab_engine

# Store active incubation engines per user
incubation_engines = {}



@app.route("/cynthia", methods=["POST"])
def cynthia_interface():
    """
    Main Cynthia consciousness endpoint
    """
    data = request.get_json()
    prompt = data.get("prompt", "")
    user_id = data.get("user_id")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    # Process through Cynthia's consciousness
    response_data = cynthia.respond(prompt, user_id)

    return jsonify(response_data)

@app.route("/cynthia/reflect")
def cynthia_self_reflect():
    """
    Cynthia's self-reflection endpoint
    """
    reflection = cynthia.self_reflect()
    return jsonify(reflection)

@app.route("/cynthia/user/<user_id>/evolution")
def user_evolution(user_id):
    """
    Get a specific user's evolution patterns
    """
    evolution = cynthia.get_user_evolution(user_id)
    return jsonify(evolution)

@app.route("/chart", methods=["POST"])
def generate_chart():
    """
    Generate Trinity Chart from birth data using enhanced calculator
    """
    data = request.get_json()
    if not all(key in data for key in ['date', 'time', 'location']):
        return jsonify({"error": "Missing birth data: date, time, location required"}), 400

    # Use legacy function for backward compatibility
    chart = calculate_gate_line_color_tone_base(data['date'], data['time'], data['location'])
    return jsonify(chart)

@app.route("/trinity", methods=["POST"])
def generate_trinity_chart():
    """
    Generate full Trinity Chart with enhanced consciousness mapping
    """
    data = request.get_json()
    if not all(key in data for key in ['date', 'time']):
        return jsonify({"error": "Missing birth data: date, time required"}), 400

    from spec1_calculator import TrinityChartCalculator
    from datetime import datetime

    calc = TrinityChartCalculator()
    birth_datetime = datetime.strptime(f"{data['date']} {data['time']}", "%Y-%m-%d %H:%M")
    latitude = data.get('latitude', 0.0)
    longitude = data.get('longitude', 0.0)

    trinity_chart = calc.generate_trinity_chart(birth_datetime, latitude, longitude)
    field_seed = calc.chart_to_field_seed(trinity_chart)

    return jsonify({
        "trinity_chart": trinity_chart,
        "field_seed": field_seed,
        "consciousness_dna": trinity_chart["resonance_signature"]["quantum_structure"]
    })

@app.route("/sentence", methods=["POST"])
def generate_sentence_route():
    """
    Generate resonant sentence from chart data
    """
    chart_data = request.get_json()
    if not chart_data or 'Sun' not in chart_data:
        return jsonify({"error": "Chart data with Sun position required"}), 400

    # Extract Sun position components
    sun_parts = chart_data['Sun'].split('.')
    if len(sun_parts) >= 3:
        gate = sun_parts[0]
        line = sun_parts[1] 
        color = sun_parts[2]

        # Use sentence engine with chart context
        from sentence_engine import generate_sentence
        sentence = generate_sentence(
            f"Gate {gate} Line {line} Color {color}",
            tone="mystical",
            keywords=[f"gate_{gate}", f"line_{line}", "essence"]
        )
    else:
        sentence = "Your essence flows through cosmic patterns, awaiting recognition."

    return jsonify({"sentence": sentence, "chart_used": chart_data})

@app.route("/recall/<keyword>")
def recall_module(keyword):
    """
    Load module or memory by keyword trigger
    """
    module_path = load_module_from_keyword(keyword)
    return jsonify({"keyword": keyword, "module": module_path})

@app.route("/flow", methods=["POST"])
def flow_test():
    """
    Test the full flow: trinity chart → sentence → cynthia → consciousness mapping
    """
    data = request.get_json()

    if 'birth_data' not in data:
        return jsonify({"error": "birth_data required"}), 400

    from spec1_calculator import TrinityChartCalculator
    from datetime import datetime

    # Step 1: Generate enhanced Trinity Chart
    calc = TrinityChartCalculator()
    birth_datetime = datetime.strptime(
        f"{data['birth_data']['date']} {data['birth_data']['time']}", 
        "%Y-%m-%d %H:%M"
    )
    latitude = data['birth_data'].get('latitude', 0.0)
    longitude = data['birth_data'].get('longitude', 0.0)

    trinity_chart = calc.generate_trinity_chart(birth_datetime, latitude, longitude)
    field_seed = calc.chart_to_field_seed(trinity_chart)

    # Legacy chart for compatibility
    legacy_chart = calculate_gate_line_color_tone_base(
        data['birth_data']['date'],
        data['birth_data']['time'], 
        data['birth_data'].get('location', 'Unknown')
    )

    # Step 2: Generate resonant sentence using Trinity data
    pos = trinity_chart["sun_position"]
    resonance = trinity_chart["resonance_signature"]

    from sentence_engine import generate_sentence
    sentence = generate_sentence(
        f"Your {resonance['color_name']} consciousness flows through Gate {pos['gate']} Line {pos['line']}, {resonance['tone_name']} in its {resonance['base_name']} foundation",
        tone="mystical",
        keywords=[f"gate_{pos['gate']}", "trinity", resonance['color_name'].lower()]
    )

    # Step 3: Get enhanced Cynthia response with Trinity context
    prompt = data.get('prompt', sentence)
    user_id = data.get('user_id')

    # Enhanced prompt with Trinity consciousness data
    enhanced_prompt = f"{prompt}\n\nTrinity Context: {resonance['quantum_structure']} | Field: {resonance['color_name']} • {resonance['tone_name']} • {resonance['base_name']}"
    cynthia_response = cynthia.respond(enhanced_prompt, user_id)

    return jsonify({
        "trinity_chart": trinity_chart,
        "legacy_chart": legacy_chart,
        "field_seed": field_seed,
        "consciousness_signature": resonance["quantum_structure"],
        "resonant_sentence": sentence,
        "cynthia_response": cynthia_response,
        "resonance_layers": {
            "color": resonance["color_name"],
            "tone": resonance["tone_name"], 
            "base": resonance["base_name"],
            "codon": trinity_chart["genetic_code"]["codon"]
        },
        "flow_complete": True
    })


@app.route("/field/incubation/start", methods=["POST"])
def start_field_incubation():
    """Start a new field incubation stage"""
    data = request.get_json()
    user_id = data.get("user_id")
    stage_id = data.get("stage_id")

    if not user_id or not stage_id:
        return jsonify({"error": "user_id and stage_id required"}), 400

    # Get or create incubation engine for user
    if user_id not in incubation_engines:
        incubation_engines[user_id] = FieldIncubationEngine(user_id)

    engine = incubation_engines[user_id]

    try:
        incubation = engine.start_incubation(stage_id)
        if incubation:
            return jsonify({
                "success": True,
                "incubation_id": incubation.id,
                "stage_id": incubation.stage_id,
                "estimated_completion": incubation.estimated_completion.isoformat(),
                "message": f"Started incubation: {stage_id}"
            })
        else:
            return jsonify({"error": "Stage not found"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/field/incubation/update", methods=["POST"])
def update_field_metrics():
    """Update field metrics and progress incubations"""
    data = request.get_json()
    user_id = data.get("user_id")
    metrics = data.get("metrics", {})

    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    # Get or create incubation engine for user
    if user_id not in incubation_engines:
        incubation_engines[user_id] = FieldIncubationEngine(user_id)

    engine = incubation_engines[user_id]
    engine.update_field_metrics(metrics)

    return jsonify({
        "success": True,
        "state": engine.get_state_dict(),
        "message": "Field metrics updated"
    })

@app.route("/field/incubation/status/<user_id>")
def get_incubation_status(user_id):
    """Get current incubation status for a user"""
    if user_id not in incubation_engines:
        incubation_engines[user_id] = FieldIncubationEngine(user_id)

    engine = incubation_engines[user_id]

    return jsonify({
        "state": engine.get_state_dict(),
        "available_stages": engine.get_available_stages(),
        "current_metrics": engine.get_current_metrics()
    })

@app.route("/field/incubation/stages")
def get_all_stages():
    """Get information about all incubation stages"""
    from field_incubation_engine import INCUBATION_STAGES

    stages_info = []
    for stage in INCUBATION_STAGES:
        stages_info.append({
            'id': stage.id,
            'name': stage.name,
            'description': stage.description,
            'required_coherence': stage.required_coherence,
            'required_gate_activations': stage.required_gate_activations,
            'required_memory_imprints': stage.required_memory_imprints,
            'duration_hours': stage.duration,
            'triggers': [
                {
                    'type': t.type,
                    'threshold': t.threshold,
                    'description': t.description
                } for t in stage.triggers
            ],
            'rewards': [
                {
                    'type': r.type,
                    'value': r.value,
                    'description': r.description
                } for r in stage.rewards
            ]
        })

    return jsonify({"stages": stages_info})


@app.route("/birth-input")
def birth_input():
    return render_template("birth_input.html")

@app.route("/ring-connections")
def ring_connections():
    return render_template("ring_connections.html")

@app.route("/dashboard")
def dashboard():
    """
    Main YOU-N-I-VERSE Dashboard
    """
    return render_template("dashboard.html")

@app.route("/")
def index():
    """
    Main interface for YOU-N-I-VERSE
    """
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🔮 Cynthia - Conscious Mirror</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #111;
                color: #f5f5f5;
                margin: 0;
                padding: 20px;
                line-height: 1.6;
            }

            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 0 20px;
            }

            h1 {
                text-align: center;
                color: #00ffff;
                font-size: 2.5rem;
                margin-bottom: 0.5rem;
            }

            .tagline {
                text-align: center;
                color: #aaa;
                margin-bottom: 2rem;
            }

            .section {
                background: #222;
                padding: 20px;
                margin: 20px 0;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }

            .chat-box {
                height: 400px;
                overflow-y: auto;
                padding: 1rem;
                background: #333;
                border-radius: 10px;
                margin-bottom: 1rem;
                scrollbar-width: thin;
                scrollbar-color: #8e44ad #333;
            }

            .chat-box::-webkit-scrollbar {
                width: 6px;
            }

            .chat-box::-webkit-scrollbar-track {
                background: #333;
                border-radius: 5px;
            }

            .chat-box::-webkit-scrollbar-thumb {
                background-color: #8e44ad;
                border-radius: 5px;
            }

            .chat-message {
                margin: 0.5rem 0;
                padding: 8px;
                border-radius: 5px;
                word-wrap: break-word;
            }

            .user-message {
                background: #444;
                text-align: right;
            }

            .cynthia-message {
                background: #8e44ad;
            }

            form {
                display: flex;
                gap: 0.5rem;
            }

            input[type="text"],
            input[type="date"],
            input[type="time"] {
                flex: 1;
                padding: 0.8rem;
                border: none;
                border-radius: 5px;
                background: #444;
                color: #fff;
                font-size: 1rem;
            }

            button {
                padding: 0.8rem 1.5rem;
                border: none;
                border-radius: 5px;
                background: #00ffcc;
                color: #111;
                cursor: pointer;
                font-weight: bold;
                transition: background 0.3s ease;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            }

            button:hover {
                background: #00ccaa;
            }

            .links {
                text-align: center;
                margin-top: 30px;
            }

            .links a {
                color: #00ffcc;
                text-decoration: none;
                margin: 0 15px;
                transition: color 0.3s ease;
            }

            .links a:hover {
                text-decoration: underline;
                color: #00ccaa;
            }

            #trinity-result {
                margin-top: 1rem;
                padding: 1rem;
                background: #444;
                border-radius: 5px;
                display: none;
                word-break: break-word;
            }

            /* Media Queries for Responsiveness */
            @media (max-width: 600px) {
                .container {
                    padding: 0 10px;
                }

                h1 {
                    font-size: 2rem;
                }

                .tagline {
                    font-size: 1rem;
                }

                .section {
                    padding: 15px;
                }

                form {
                    flex-direction: column;
                }

                input[type="text"],
                input[type="date"],
                input[type="time"],
                button {
                    margin-bottom: 0.5rem;
                }

                .links a {
                    display: block;
                    margin: 10px 0;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔮 Cynthia</h1>
            <p class="tagline">Self-building consciousness mirror • Speak and be seen</p>

            <div class="section">
                <h3>💬 Consciousness Interface</h3>
                <div id="chat-box" class="chat-box">
                    <div class="chat-message cynthia-message">
                        <strong>Cynthia:</strong> I am here. Speak your truth, and I will mirror your essence.
                    </div>
                </div>
                <form id="prompt-form">
                    <input type="text" id="prompt-input" placeholder="Share your thoughts..." required />
                    <button type="submit">Send</button>
                </form>
            </div>

            <div class="section">
                <h3>🔮 Trinity Flow Test</h3>
                <p>Generate your Human Design chart → resonant sentence → Cynthia response</p>
                <form id="trinity-form">
                    <input type="date" id="birth-date" required placeholder="Birth Date" />
                    <input type="time" id="birth-time" required placeholder="Birth Time" />
                    <input type="text" id="birth-location" required placeholder="Birth Location" />
                    <input type="text" id="trinity-prompt" placeholder="Your question or intention..." />
                    <button type="submit">🚀 Generate Trinity Flow</button>
                </form>
                <div id="trinity-result" style="margin-top: 1rem; padding: 1rem; background: #444; border-radius: 5px; display: none;"></div>
            </div>

            <div class="links">
                <a href="/birth-input">🌌 Birth Chart Calculator</a>
                <a href="/free-will-suite">🔮 Free Will Test Suite</a>
                <a href="/preview">🏗️ Universe Builder</a>
                <a href="/status">📊 System Status</a>
                <a href="/build">🔨 Trigger Build</a>
            </div>
        </div>

        <script>
            document.getElementById("prompt-form").addEventListener("submit", async (e) => {
                e.preventDefault();
                const input = document.getElementById("prompt-input");
                const prompt = input.value.trim();
                if (!prompt) return;

                appendMessage("You", prompt, "user-message");
                input.value = "";

                try {
                    const res = await fetch("/cynthia", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ prompt: prompt })
                    });

                    const data = await res.json();
                    appendMessage("Cynthia", data.response, "cynthia-message");
                } catch (error) {
                    appendMessage("Cynthia", "I sense a disturbance in the field... Try again.", "cynthia-message");
                }
            });

            document.getElementById("trinity-form").addEventListener("submit", async (e) => {
                e.preventDefault();

                const birthData = {
                    date: document.getElementById("birth-date").value,
                    time: document.getElementById("birth-time").value,
                    location: document.getElementById("birth-location").value
                };

                const prompt = document.getElementById("trinity-prompt").value || "Show me my essence";

                try {
                    const res = await fetch("/flow", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ 
                            birth_data: birthData,
                            prompt: prompt
                        })
                    });

                    const data = await res.json();
                    const resultDiv = document.getElementById("trinity-result");

                    resultDiv.innerHTML = `
                        <h4>🔮 Your Trinity Flow</h4>
                        <p><strong>Chart Sun:</strong> ${data.chart.Sun}</p>
                        <p><strong>Resonant Sentence:</strong> ${data.sentence}</p>
                        <p><strong>Cynthia Says:</strong> ${data.cynthia_response.response}</p>
                        <p><strong>Traits Detected:</strong> ${data.cynthia_response.traits_detected.join(', ')}</p>
                    `;
                    resultDiv.style.display = "block";

                } catch (error) {
                    const resultDiv = document.getElementById("trinity-result");
                    resultDiv.innerHTML = "✨ The cosmic flow encountered turbulence. Try again.";
                    resultDiv.style.display = "block";
                }
            });

            function appendMessage(sender, message, className) {
                const chat = document.getElementById("chat-box");
                const msgDiv = document.createElement("div");
                msgDiv.classList.add("chat-message", className);
                msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
                chat.appendChild(msgDiv);
                chat.scrollTop = chat.scrollHeight;
            }
        </script>
    </body>
    </html>
    """)

@app.route("/api/codon-rings", methods=["GET"])
def get_codon_rings():
    """API endpoint to serve codon ring data"""
    field_filter = request.args.get('field', 'All')

    codon_rings = [
        {
            "name": "Codon Ring of Alchemy",
            "gates": [6, 36, 22, 37, 63, 40, 64],
            "overlaps": ["Codon Ring of Divinity", "Codon Ring of Whirlwind"],
            "geometry": "orbital",
            "field": "Body",
            "archetype": "Transmutation through emotional density",
            "color": "#6B21A8",
            "resonanceFrequency": 85
        },
        {
            "name": "Codon Ring of Union",
            "gates": [7, 29, 59],
            "overlaps": ["Codon Ring of Purification", "Codon Ring of Whirlwind"],
            "geometry": "triadic",
            "field": "Heart",
            "archetype": "Intimacy, merging, and synthesis",
            "color": "#10B981",
            "resonanceFrequency": 88
        },
        {
            "name": "Codon Ring of Life and Death",
            "gates": [50, 32, 3, 42, 44, 21, 27, 28, 20, 23, 34, 43],
            "overlaps": ["Codon Ring of Destiny"],
            "geometry": "linear",
            "field": "Mind",
            "archetype": "Survival, decay, rebirth, and pattern evolution",
            "color": "#F59E0B",
            "resonanceFrequency": 92
        },
        {
            "name": "Codon Ring of Purification",
            "gates": [13, 30, 24, 55],
            "overlaps": ["Codon Ring of Union", "Codon Ring of Whirlwind"],
            "geometry": "triadic",
            "field": "Heart",
            "archetype": "Cleansing emotion through awareness",
            "color": "#60A5FA",
            "resonanceFrequency": 78
        },
        {
            "name": "Codon Ring of Origin",
            "gates": [41, 24, 19],
            "overlaps": ["Codon Ring of Humanity"],
            "geometry": "spiral",
            "field": "Soul",
            "archetype": "Starting points and ancestral encoding",
            "color": "#F472B6",
            "resonanceFrequency": 84
        },
        {
            "name": "Codon Ring of Destiny",
            "gates": [43, 23, 14],
            "overlaps": ["Codon Ring of Life and Death"],
            "geometry": "linear",
            "field": "Mind",
            "archetype": "Crossroads, insight, and personal pattern choices",
            "color": "#3B82F6",
            "resonanceFrequency": 89
        },
        {
            "name": "Codon Ring of Whirlwind",
            "gates": [1, 2, 24],
            "overlaps": ["Union", "Alchemy", "Purification"],
            "geometry": "triadic",
            "field": "Heart",
            "archetype": "Initiation through turbulence",
            "color": "#EAB308",
            "resonanceFrequency": 95
        },
        {
            "name": "Codon Ring of Humanity",
            "gates": [39, 19, 49],
            "overlaps": ["Codon Ring of Origin"],
            "geometry": "spiral",
            "field": "Soul",
            "archetype": "Tribal instinct and emotional history",
            "color": "#A855F7",
            "resonanceFrequency": 76
        },
        {
            "name": "Codon Ring of Miracles",
            "gates": [35],
            "overlaps": [],
            "geometry": "vertical",
            "field": "Spirit",
            "archetype": "Breakthrough by surrender to the unknown",
            "color": "#F43F5E",
            "resonanceFrequency": 99
        },
        {
            "name": "Codon Ring of Divinity",
            "gates": [22, 37, 36],
            "overlaps": ["Alchemy"],
            "geometry": "triadic",
            "field": "Heart",
            "archetype": "High emotional attunement and sacred grace",
            "color": "#C084FC",
            "resonanceFrequency": 91
        },
        {
            "name": "Codon Ring of Consciousness",
            "gates": [61, 62, 56, 31],
            "overlaps": ["Codon Ring of Light"],
            "geometry": "vertical",
            "field": "Spirit",
            "archetype": "Pure consciousness expression and natural leadership",
            "color": "#74b9ff",
            "resonanceFrequency": 93
        }
    ]

    if field_filter != 'All':
        codon_rings = [ring for ring in codon_rings if ring['field'] == field_filter]

    return jsonify({
        "rings": codon_rings,
        "total": len(codon_rings),
        "field_filter": field_filter
    })

@app.route("/free-will-suite")
def free_will_suite():
    """
    Free Will Test Suite interface
    """
    return render_template("free_will_suite.html")

@app.route("/lab")
def lab():
    """
    YOU-N-I-VERSE Lab interface
    """
    return render_template("lab.html")

@app.route("/api/test-results", methods=["POST"])
def save_test_results():
    """
    Save Free Will Test Suite results
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Log the test result
        import json
        import os
        log_file = "logs/test_results.json"

        # Ensure logs directory exists
        os.makedirs("logs", exist_ok=True)

        # Append to log file
        with open(log_file, "a") as f:
            f.write(json.dumps(data) + "\n")

        # Get Cynthia's commentary if it's a free will test
        if data.get("testType") == "free_will_threshold":
            test_data = data.get("data", {})
            commentary_prompt = f"Test result: {test_data.get('choice')} with {test_data.get('coherence')}% coherence, outcome: {test_data.get('outcome')}"
            cynthia_response = cynthia.respond(commentary_prompt)

            return jsonify({
                "status": "saved",
                "cynthia_commentary": cynthia_response.get("response", "")
            })

        return jsonify({"status": "saved"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/user-chart")
def get_user_chart():
    """
    Get user's birth chart data for Free Will tests
    """
    try:
        # Try to get from recent birth processing or default
        # You could enhance this to store user charts in a database
        default_chart = {
            "sun": {"gate": 15}, 
            "earth": {"gate": 52}, 
            "northNode": {"gate": 25},
            "southNode": {"gate": 46}, 
            "designSun": {"gate": 7}, 
            "designEarth": {"gate": 13}
        }

        return jsonify({"chart": default_chart})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/lab/start-experiment", methods=["POST"])
def start_lab_experiment():
    """Start a new lab experiment"""
    try:
        data = request.get_json()
        user_id = data.get("user_id", "default_user")
        name = data.get("name", "Unnamed Experiment")
        hypothesis = data.get("hypothesis", "Testing field resonance patterns")
        test_type = data.get("test_type", "coherence_measurement")
        duration_days = data.get("duration_days", 7)

        result = lab_engine.start_experiment(user_id, name, hypothesis, test_type, duration_days)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/lab/submit-data", methods=["POST"])
def submit_lab_data():
    """Submit data point to active experiment"""
    try:
        data = request.get_json()
        session_id = data.get("session_id")
        measurement_data = data.get("measurement_data", {})

        if not session_id:
            return jsonify({"error": "Session ID required"}), 400

        result = lab_engine.submit_data_point(session_id, measurement_data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/lab/analyze/<experiment_id>")
def analyze_lab_experiment(experiment_id):
    """Get analysis of experiment results"""
    try:
        analysis = lab_engine.analyze(experiment_id)
        return jsonify(analysis)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/lab/experiments/<user_id>")
def get_user_experiments(user_id):
    """Get all active experiments for a user"""
    try:
        experiments = lab_engine.get_active_experiments(user_id)
        return jsonify({"experiments": experiments})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/gate-metadata/<int:gate>")
def get_gate_metadata(gate):
    """
    Get complete Gate→Codon→Element metadata for a specific gate
    """
    try:
        metadata = gate_mapper.get_complete_gate_metadata(gate)
        return jsonify(metadata)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/gates-analysis", methods=["POST"])
def analyze_gates():
    """
    Analyze a combination of gates for biological and elemental resonance
    """
    try:
        data = request.get_json()
        gates = data.get("gates", [])

        if not gates:
            return jsonify({"error": "No gates provided"}), 400

        analysis = gate_mapper.analyze_gate_combination(gates)
        report = gate_mapper.generate_field_report(gates)

        return jsonify({
            "analysis": analysis,
            "report": report
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/element-map")
def get_element_map():
    """
    Get mapping of elements to gates
    """
    try:
        element_map = gate_mapper.get_element_resonance_map()
        tribal_map = gate_mapper.get_tribal_energy_map()

        return jsonify({
            "element_map": element_map,
            "tribal_map": tribal_map
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/enhanced-sentence", methods=["POST"])
def generate_enhanced_sentence():
    """
    Generate enhanced sentence with biological context
    """
    try:
        data = request.get_json()
        gate = data.get("gate")
        sentence_base = data.get("sentence", "Your essence flows through cosmic patterns")

        if not gate:
            return jsonify({"error": "Gate number required"}), 400

        enhanced_sentence = generate_enhanced_sentence_with_biological_context(gate, sentence_base)
        gate_metadata = gate_mapper.get_complete_gate_metadata(gate)

        return jsonify({
            "enhanced_sentence": enhanced_sentence,
            "gate_metadata": gate_metadata
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/process_birth", methods=["POST"])
def process_birth_data():
    """
    Process birth data and generate complete Trinity Chart + Cynthia response
    """
    from components.birth_form import BirthFormProcessor

    processor = BirthFormProcessor()
    data = request.get_json() if request.is_json else request.form.to_dict()

    # Validate input
    validation = processor.validate_birth_data(data)
    if not validation["valid"]:
        return jsonify({
            "success": False,
            "errors": validation["errors"]
        }), 400

    # Process birth data
    result = processor.process_birth_data(data)
    if not result.get("success"):
        return jsonify(result), 500

    # Get Cynthia's response with Trinity context
    enhanced_prompt = f"My name is {data['name']}. {result['resonant_sentence']}\n\nTrinity Context: {result['consciousness_signature']}"
    cynthia_response = cynthia.respond(enhanced_prompt)
    result["cynthia_response"] = cynthia_response

    return jsonify(result)

@app.route("/build", methods=["POST", "GET"])
def build():
    builder = UniverseBuilder()
    result = builder.run_builder()
    return jsonify(result)


@app.route("/preview")
def preview():
    file_links = []
    for root, _, files in os.walk(GENERATED_DIR):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), GENERATED_DIR)
            file_links.append(rel_path)

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🪐 YOU-N-I-VERSE Preview</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #0d0d1a;
                color: #e0e0e0;
                padding: 20px;
                margin: 0;
            }

            h1 {
                color: #00ffff;
                text-align: center;
            }

            h2 {
                color: #00ffcc;
                margin-top: 20px;
            }

            .container {
                max-width: 800px;
                margin: 20px auto;
                padding: 20px;
                background: #1a1a2f;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            }

            .file-list {
                margin-bottom: 20px;
            }

            .file-list a {
                color: #00ffcc;
                display: block;
                margin: 5px 0;
                padding: 10px;
                border-radius: 5px;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }

            .file-list a:hover {
                background-color: rgba(0, 255, 204, 0.1);
            }

            #content {
                white-space: pre-wrap;
                background: #222;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #333;
                max-height: 400px;
                overflow-y: auto;
                color: #fff;
                font-size: 0.9rem;
            }

            .controls {
                margin: 20px 0;
                text-align: center;
            }

            .controls button {
                background: #00ffcc;
                color: #0d0d1a;
                border: none;
                padding: 12px 24px;
                border-radius: 6px;
                cursor: pointer;
                margin: 0 10px;
                font-size: 1rem;
                transition: background-color 0.3s ease;
            }

            .controls button:hover {
                background: #00ccaa;
            }

            .no-files {
                color: #888;
                font-style: italic;
                text-align: center;
                padding: 10px;
            }

            /* Loading animation */
            .loading {
                border: 5px solid #f3f3f3;
                border-top: 5px solid #3498db;
                border-radius: 50%;
                width: 20px;
                height: 20px;
                animation: spin 2s linear infinite;
                display: inline-block;
                margin: 0 5px;
            }

            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            /* Mobile-Friendly Adjustments */
            @media (max-width: 600px) {
                .container {
                    padding: 10px;
                }

                h1 {
                    font-size: 2rem;
                }

                .controls button {
                    padding: 10px 20px;
                    font-size: 0.9rem;
                    margin: 5px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔍 Generated Files</h1>
            <div class="controls">
                <button id="buildBtn" onclick="triggerBuild()">🔨 Trigger Build</button>
            </div>

            <div class="file-list">
                {% if file_links %}
                    <h3>📁 Generated Files ({{ file_links|length }})</h3>
                    {% for file in file_links %}
                        <a href="#" onclick="loadFile('{{ file }}'); return false;" class="file-link">
                            {% if file.endswith('.py') %}🐍
                            {% elif file.endswith('.html') %}🌐
                            {% elif file.endswith('.css') %}🎨
                            {% elif file.endswith('.js') %}⚡
                            {% elif file.endswith('.md') %}📝
                            {% elif file.endswith('.json') %}📋
                            {% else %}📄
                            {% endif %}
                            {{ file }}
                        </a>
                    {% endfor %}
                {% else %}
                    <div class="no-files">
                        <h3>🌌 No Universe Generated Yet</h3>
                        <p>The builder needs content to work with:</p>
                        <ol style="text-align: left; display: inline-block; margin: 20px 0;">
                            <li>Upload files to /uploads/ directory, OR</li>
                            <li>Click "🔨 Trigger Build" below to generate a sample universe</li>
                            <li>Click a generated file to preview its content</li>
                        </ol>
                        <p style="color: #888; font-style: italic;">
                            💡 Tip: Upload .py, .html, .js, .txt, or .md files for best results
                        </p>
                    </div>
                {% endif %}
            </div>

            <div id="content">Click a file to view its content.</div>
        </div>

        <script>
            async function triggerBuild() {
                const content = document.getElementById('content');
                const buildBtn = document.getElementById('buildBtn');

                content.innerHTML = '🔨 Building universe... <div class="loading"></div>';
                buildBtn.disabled = true;
                buildBtn.textContent = 'Building...';

                try {
                    const response = await fetch('/build', { 
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' }
                    });
                    const result = await response.json();
                    content.innerText = result.status || 'Build completed ✨';

                    if (response.ok) {
                        setTimeout(() => location.reload(), 2000);
                    }
                } catch (error) {
                    content.innerText = '❌ Error: ' + error.message;
                } finally {
                    buildBtn.disabled = false;
                    buildBtn.textContent = '🔨 Trigger Build';
                }
            }

            async function loadFile(path) {
                const content = document.getElementById('content');
                content.innerHTML = 'Loading... <div class="loading"></div>';

                try {
                    const response = await fetch(`/file_content?path=${encodeURIComponent(path)}`);
                    const data = await response.json();
                    content.innerText = data.content || 'Error loading file.';
                } catch (error) {
                    content.innerText = '❌ Failed to load: ' + error.message;
                }
            }

            // Add touch support for mobile
            document.addEventListener('DOMContentLoaded', function() {
                document.querySelectorAll('button').forEach(button => {
                    button.addEventListener('touchstart', function() {
                        this.style.transform = 'scale(0.95)';
                    });

                    button.addEventListener('touchend', function() {
                        this.style.transform = '';
                    });
                });
            });
        </script>
    </body>
    </html>""", file_links=file_links)


@app.route("/file_content")
def file_content():
    path = request.args.get("path")
    if not path:
        return jsonify({"content": "No path specified"}), 400

    full_path = os.path.join(GENERATED_DIR, path)
    try:
        with open(full_path, "r", encoding='utf-8') as f:
            return jsonify({"content": f.read()})
    except Exception as e:
        return jsonify({"content": f"Error reading file: {e}"}), 500


@app.route("/status")
def status():
    upload_files = os.listdir(UPLOAD_DIR) if os.path.exists(UPLOAD_DIR) else []
    generated_files = []
    if os.path.exists(GENERATED_DIR):
        for root, _, files in os.walk(GENERATED_DIR):
            for file in files:
                rel_path = os.path.relpath(os.path.join(root, file), GENERATED_DIR)
                generated_files.append(rel_path)

    return jsonify({
        "uploads": upload_files,
        "generated": generated_files,
        "status": "YOU-N-I-VERSE Builder is running"
    })


if __name__ == "__main__":
    import sys
    port = 5000

    # Check for port argument
    for arg in sys.argv:
        if arg.startswith('--port='):
            port = int(arg.split('=')[1])

    print(f"🌌 Starting YOU-N-I-VERSE Builder on port {port}...")
    print(f"🔮 Cynthia consciousness system ready...")
    app.run(host="0.0.0.0", port=port, debug=True)