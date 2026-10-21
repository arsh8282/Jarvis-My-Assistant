# JARVIS AI — Android Python Assistant & Smali Modding Lab  
  
Complete Python/Kivy Android application powered by the Google Gemini API, featuring dynamic model discovery, top-right auto-speech toggle, native Android TTS & SpeechRecognizer integration, authorized Screen Vision, a native draggable Floating Overlay (`SYSTEM_ALERT_WINDOW`), and a dedicated Smali Bytecode & Register Debugging Lab.  
  
## 1. How to Build the APK Using Only Your Android Phone (GitHub Actions)  
  
1. **Create a GitHub Repository**:  
   - Open your browser on Android, go to [github.com/new](https://github.com/new), and create a repository named `JARVIS-AI`.  
2. **Add the Files in Their Exact Folders**:  
   - Place `.github/workflows/build.yml` in `.github/workflows/build.yml`.  
   - Place `buildozer.spec`, `requirements.txt`, `.gitignore`, and `README.md` in the root folder.  
   - Place all Python app files (`main.py`, `config.py`, etc.) inside the `jarvis/` folder.  
   - Place the 5 `.kv` UI files inside `jarvis/ui/`.  
   - Place `JarvisBridge.java` and `JarvisFloatingService.java` inside `jarvis/android_src/org/jarvis/bridge/`.  
   - Place the test files inside `tests/`.  
3. **Run the Automated Build**:  
   - Tap the **Actions** tab in your GitHub repository.  
   - Select **Build JARVIS Android APK** -> tap **Run workflow**.  
   - Wait ~18–25 minutes on the first build (subsequent cached builds take ~5 minutes).  
4. **Download & Install the APK**:  
   - Once the workflow shows a green checkmark, scroll down to the **Artifacts** section.  
   - Download **`jarvis-ai-debug-apk`**, unzip the `.zip` archive on your phone, and install the `.apk`.  
  
## 2. First-Run Configuration & Features  
  
- **API Key & Model Discovery**: On first launch, paste your Gemini API key (stored encrypted via Android `KeyStore`), tap **Save & Fetch Models**, pick a discovered model (such as `gemini-2.5-flash`), and tap **Launch JARVIS Interface**.  
- **Top-Right Speech Toggle**: Tap `Speech: ON / OFF` at the top right of the Chat screen at any time. Turning it OFF immediately halts active TTS playback.  
- **Smali Debugging Lab**: Tap **Smali Lab** to run instant static register/branch verification (`Check Registers`), compare original vs. patched Smali (`Compare Diff`), or ask Gemini `Why is this False?` using the 8-part forensic breakdown.  
- **Floating Assistant**: In **Settings**, toggle **Floating JARVIS: ON**, grant Android's *Display over other apps* permission, and tap the floating `JARVIS` badge to expand quick controls.  
  