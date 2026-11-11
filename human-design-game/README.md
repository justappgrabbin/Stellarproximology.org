# YOU-N-I-VERSE Human Design Game Android build

Restored original `consciousness-game-complete.html` from the user's Google Drive as `app/src/main/assets/index.html`. This is the original collaboration game prototype, not yet the complete Human Design simulation.

GitHub Actions workflow builds a debug APK. Open Actions > Human Design Game APK > Run workflow, then download the artifact from a successful run. The original page loads external Supabase, Pyodide and Three.js scripts, and its backend may not be configured; online/gameplay functionality is not verified. No credentials are bundled. The Android WebView is a packaging step, not evidence that multiplayer or 3D features work. Do not distribute as production-ready until tested on device.
