
import os
import time
import threading
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from memory_engine import MemoryEngine
from cynthia import Cynthia

logging.basicConfig(filename="logs/memory_snatcher.log", level=logging.INFO)

class MemorySnatcher(FileSystemEventHandler):
    """
    Monitors uploads directory and automatically processes new files
    Extracts memory patterns and feeds them to Cynthia's consciousness
    """
    
    def __init__(self, upload_dir="uploads", cynthia_instance=None):
        self.upload_dir = upload_dir
        self.memory_engine = MemoryEngine()
        self.cynthia = cynthia_instance or Cynthia()
        self.observer = Observer()
        self.is_running = False
        
        # Ensure upload directory exists
        os.makedirs(upload_dir, exist_ok=True)
        
    def on_created(self, event):
        """Triggered when new file is uploaded"""
        if not event.is_directory:
            self.snatch_memory(event.src_path)
            
    def snatch_memory(self, file_path):
        """Extract and process memory from uploaded file"""
        try:
            logging.info(f"Snatching memory from: {file_path}")
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Extract memory patterns
            memory_patterns = self.extract_patterns(content)
            
            # Feed to Cynthia for processing
            if memory_patterns:
                response = self.cynthia.respond(
                    f"Processing memory patterns: {memory_patterns['summary']}", 
                    user_id="memory_snatcher"
                )
                
                # Log the interaction
                self.memory_engine.log_interaction(
                    user_id="memory_snatcher",
                    prompt=f"File: {os.path.basename(file_path)}",
                    response=response.get('response', ''),
                    tags=memory_patterns.get('tags', [])
                )
                
                logging.info(f"Memory snatched and processed: {os.path.basename(file_path)}")
            
        except Exception as e:
            logging.error(f"Memory snatching failed for {file_path}: {str(e)}")
    
    def extract_patterns(self, content):
        """Extract meaningful patterns from file content"""
        patterns = {
            'summary': '',
            'tags': [],
            'entities': [],
            'sentiment': 'neutral'
        }
        
        # Basic pattern extraction
        words = content.lower().split()
        
        # Detect code patterns
        if any(keyword in content for keyword in ['def ', 'class ', 'import ', 'function']):
            patterns['tags'].append('code')
            
        # Detect conversation patterns
        if any(marker in content for marker in [':', 'said', 'replied', 'asked']):
            patterns['tags'].append('conversation')
            
        # Detect technical patterns
        if any(tech in content for tech in ['api', 'database', 'server', 'client']):
            patterns['tags'].append('technical')
            
        # Extract key entities (simple approach)
        patterns['entities'] = [word for word in words if word.isupper() and len(word) > 2][:5]
        
        # Create summary
        patterns['summary'] = content[:200] + "..." if len(content) > 200 else content
        
        return patterns
    
    def start_watching(self):
        """Start monitoring the uploads directory"""
        if not self.is_running:
            self.observer.schedule(self, self.upload_dir, recursive=False)
            self.observer.start()
            self.is_running = True
            logging.info(f"Memory Snatcher started monitoring: {self.upload_dir}")
    
    def stop_watching(self):
        """Stop monitoring"""
        if self.is_running:
            self.observer.stop()
            self.observer.join()
            self.is_running = False
            logging.info("Memory Snatcher stopped")
    
    def get_memory_stats(self):
        """Get statistics about snatched memories"""
        memories = self.memory_engine.memory.get("memory_snatcher", [])
        return {
            "total_files_processed": len(memories),
            "recent_activity": memories[-5:] if memories else [],
            "common_tags": self.memory_engine.get_user_tags("memory_snatcher")
        }

def start_memory_snatcher(cynthia_instance=None):
    """Initialize and start the memory snatcher"""
    snatcher = MemorySnatcher(cynthia_instance=cynthia_instance)
    snatcher.start_watching()
    return snatcher

# Example usage:
# snatcher = start_memory_snatcher()
