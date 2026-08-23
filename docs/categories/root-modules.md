# ⚡ Root, Magisk & KernelSU Modules

### Root utilities, Magisk/KernelSU/APatch modules, and Xposed enhancements.

[⬅️ **Back to Main Catalog**](../../README.md) • [📚 **All Apps Index**](../all-apps.md)

> **Total Apps in Category:** `171`

---

### 📦 Switcher 5G

> **Categories:** `#android` `#shizuku` `#5g` `#utilities`

The fastest way to switch your Android network mode — no root required. A minimalist, open-source utility built with Kotlin & Jetpack Compose. Switch between 5G SA, 5G NSA, and 4G LTE in a single tap, with full Material You theming and Quick Settings tile support.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/13521](https://t.me/popCLOUDS/13521)
- 👤 **Developer:** [shreyagarwal72](https://github.com/shreyagarwal72/)

<details>
<summary><b>✨ Key Features (5)</b> — <i>Click to expand</i></summary>

- 1-tap mode switching (Shizuku, no root)
- Manual fallback via system RadioInfo
- Quick Settings tile + deep link/broadcast support
- Full Material You theming, AMOLED black
- Backup/restore settings, in-app update checker

</details>

<details>
<summary><b>🖼️ Preview Screenshots & Media (1)</b> — <i>Click to view images & decide if you want to use this app</i></summary>

#### 📸 Cover / Preview
<p align="center"><img src="../../assets/apps/switcher-5g/cover.jpg" alt="Cover / Preview" style="max-height: 480px; max-width: 100%; border-radius: 8px; margin: 8px auto;" /></p>

</details>


---

### 📦 Smooth Optimizer

> **Categories:** `#Android` `#Root` `#Modules`

Optimizes your Android device for smoother scrolling and animations.

- 🐙 **Source Code:** [https://github.com/NoneBaiano/SmoothOptimizer](https://github.com/NoneBaiano/SmoothOptimizer)
- 👤 **Developer:** [NoneBaiano](https://github.com/NoneBaiano)

<details>
<summary><b>✨ Key Features (4)</b> — <i>Click to expand</i></summary>

- Reduces system animation duration to 0.75x (faster animations)
- Increases touch event rate for more responsive touch
- Adjusts fling velocity for smoother scrolling
- Enables high refresh rate support

</details>


---

### 📦 Root My Galaxy

> **Categories:** `#Samsung` `#Root` `#Tools`

Root My Galaxy is a lightweight utility that enables temporary, exploit-based root access on supported Samsung Galaxy devices—without permanently unlocking the bootloader or tripping Knox. It provides elevated privileges while preserving core Samsung security features, making it ideal for advanced users, developers, and power users.

- 🐙 **Source Code:** [https://github.com/BuSung-dev/Root-My-Galaxy](https://github.com/BuSung-dev/Root-My-Galaxy)
- 👤 **Developer:** [BuSung-dev](https://github.com/BuSung-dev)


---

### 📦 Revanced & Morphe Builder

> **Categories:** `#apps` `#web` `#android` `#revanced` `#morphe`

ReVanced & Morphe Builder is an automated build system for creating the latest patched Android apps and Magisk/KernelSU modules. By integrating multiple patch ecosystems and rebuilding releases 24/7, it delivers a fast, reliable, and hassle-free way to stay up to date with the newest enhancements.

- 🐙 **Source Code:** [https://github.com/nullcpy/rvb](https://github.com/nullcpy/rvb)
- 👤 **Developer:** [nullcpy](https://github.com/nullcpy)

<details>
<summary><b>✨ Key Features (8)</b> — <i>Click to expand</i></summary>

- **Automated Builds** — Continuously generates the latest patched apps and modules.
- **Multiple Patch Ecosystems** — Supports ReVanced, ReVanced Extended (RVX), Morphe, RVX Morphed, and ReVanced Advanced.
- **Ready-to-Use Releases** — Download pre-built APKs and Magisk/KernelSU modules without manual patching.
- **Always Up-to-Date** — Rebuilds automatically whenever new patches or app versions are available.
- **Fast & Reliable** — CI-powered build pipeline for consistent, reproducible releases.
- **Wide App Support** — Builds patched versions for a variety of supported Android applications.
- Root & Non-Root Options Provides both standalone APKs and root module variants where available.
- **Open Source** — Transparent development with publicly available source code.

</details>


---

### 📦 DeepDoze-Enforcer

> **Categories:** `#android` `#root` `#magisk` `#ksu` `#doze` `#BatterySaver`

DeepDoze Enforcer is a lightweight Magisk/KernelSU module that instantly forces Android into deep Doze mode whenever the screen is locked, reducing background activity, lowering CPU usage, and minimizing battery drain.

- 🐙 **Source Code:** [https://github.com/Azyrn/DeepDoze-Enforcer](https://github.com/Azyrn/DeepDoze-Enforcer)
- 👤 **Developer:** [Azyrn](https://github.com/Azyrn)

<details>
<summary><b>✨ Key Features (18)</b> — <i>Click to expand</i></summary>

- Android 8.0 (API 26) and newer
- Magisk 24.0+, KernelSU 1.0+, APatch
- **Works on most phones** — no kernel modifications, framework level only
- Forces the device into deep Doze shortly after you lock the phone
- Re-enforces during long locked periods via periodic maintenance
- Moves non-whitelisted apps into the rare (gentle) or restricted (balanced / aggressive) standby bucket while the phone is locked
- Denies the RUN_ANY_IN_BACKGROUND app-op for non-whitelisted apps in balanced and aggressive modes
- In aggressive mode, also force-stops idle non-foreground apps
- **The restricted bucket is what the OS uses to defer their jobs, alarms and network** — the module sets the bucket, it does not cancel jobs or alarms directly
- Everything is reverted (buckets back to active, app-op re-allowed) the moment you unlock
- No dedicated GMS / GSF throttling is currently implemented
- **Google packages are handled like other apps** — protected when whitelisted, otherwise eligible for the same while-locked background restrictions
- Does not change Wi-Fi, Bluetooth scanning, network scoring, location mode or sensor settings
- Savings while locked come from Doze enforcement, CPU throttling and app standby / background-run restrictions for eligible third-party apps
- Battery-saver / low-power mode
- Location mode and toggles
- Account sync preferences
- Animation scales, screen-off timeout and always-on display

</details>


---

### 📦 Kill My Apps

> **Categories:** `#Android` `#Hibernator` `#Root` `#Shizuku`

Kill My Apps is a lightweight utility designed to terminate background processes, helping you extend battery life, boost gaming performance and reclaim system resources. It work with Root and Shizuku. Without it, you can still use the app, but you'll need to manually force-stop target apps.

- 🐙 **Source Code:** [https://github.com/dedeadend/KillMyApps](https://github.com/dedeadend/KillMyApps)
- 👤 **Developer:** [Ehsan Nasiri](https://github.com/dedeadend)

<details>
<summary><b>✨ Key Features (7)</b> — <i>Click to expand</i></summary>

- ****One-Click Optimization**** — Terminate all background activities instantly.
- ****Killer Modes**** — Support Root and Shizuku for an automated app termination process.
- ****Exclusion List**** — Whitelist your important apps to keep them running.
- ****Smart Filtering**** — Categorize apps by User, Launchable, or System processes.
- ****Battery Saver**** — Reduce power consumption by eliminating idle app activities.
- ****Performance Boost**** — Free up RAM and CPU for high-demand tasks like gaming.
- ****Clean UI**** — Simple and intuitive Material Design interface.

</details>


---

### 📦 Shevery

> **Categories:** `#Android` `#ADB` `#Root` `#Tools`

A modernized fork of Shizuku Manager with a Jetpack Compose + Material 3 Expressive UI, Dhizuku device-owner bridging, an upgraded ADB shell console with Gemini explanations, Android 16/17 target work, and an ADB Modules system for installing and managing ZIP-based modules.

- 🐙 **Source Code:** [https://github.com/HmnDev-Tech/shevery](https://github.com/HmnDev-Tech/shevery)
- 👤 **Developer:** [HmnDev-Tech](https://github.com/HmnDev-Tech)

<details>
<summary><b>✨ Key Features (29)</b> — <i>Click to expand</i></summary>

- Jetpack Compose manager UI with Material 3 Expressive components, motion, switches, and rounded icon treatment.
- ****Dhizuku Experimental Support**** — Dedicated Device-Owner bridging system available inside Laboratory features.
- **Better shell/adb based "Comput"** feature with Gemini Explaination.
- Android 16/17 target work with current preview SDK/build tooling in this fork.
- ADB Modules screen for installing and managing ZIP modules.
- **Module features** — module.prop, banner, enable/disable switch, action.sh, policy-gated service.sh, local WebUI, delete, path checks, size limits, output limits, and last-run logs.
- **Module policy settings** — Safe mode, Full access, and background action control.
- Debug test module under test-modules/adb-test-module.zip.
- [ADB Modules guide](docs/adb-modules-guide.md)
- [ADB Modules API reference](docs/adb-modules-api.md)
- [Shizuku Connectors API](docs/shizuku-connectors.md)
- [Android 17 Compatibility](docs/android-17-compatibility.md)
- **Extremely slow** (Multiple process creation)
- Needs to process texts (**Super unreliable**)
- The possibility is limited to available commands
- Even if ADB has sufficient permissions, the app requires root privileges to run
- *📸 Click to open Screenshot Gallery**
- ADB permissions are limited
- Hidden API limitation from Android 9
- Android 8.0 & ADB
- Direct use of transactRemote requires attention
- The API may be different under different Android versions, please be sure to check it carefully. Also, the android.app.IActivityManager has the aidl form in API 26 and later, and android.app.IActivityManager$Stub exists only on API 26.
- SystemServiceHelper.getTransactionCode may not get the correct transaction code, such as android.content.pm.IPackageManager$Stub.TRANSACTION_getInstalledPackages does not exist on API 25 and there is android.content.pm.IPackageManager$Stub.TRANSACTION_getInstalledPackages_47 (this situation has been dealt with, but it is not excluded that there may be other circumstances). This problem is not encountered with the ShizukuBinderWrapper method.
- Clone with git clone --recurse-submodules
- **Run gradle task** — manager:assembleDebug or :manager:assembleRelease
- You are **FORBIDDEN** to use manager/src/main/res/mipmap*/ic_launcher*.png image files, unless for displaying Shizuku itself.
- You are **FORBIDDEN** to use Shizuku as app name or use moe.shizuku.privileged.api as application id or declare moe.shizuku.manager.permission.* permission.
- **[Nightzuku](https** — //github.com/kerneldroid/Nightzuku) - for parts of App UI and Android 17 support.
- **[Shizuku](https** — //github.com/rikkaapps/Shizuku) - for Shizuku API and main sources.

</details>


---

### 📦 openclaw-android

> **Categories:** `#AI` `#Android` `#homelab` `#Openclaw`

Run OpenClaw on Android with a single command — no proot, no Linux

- 🐙 **Source Code:** [https://github.com/AidanPark/openclaw-android](https://github.com/AidanPark/openclaw-android)
- 👤 **Developer:** [AidanPark](https://github.com/AidanPark)

<details>
<summary><b>✨ Key Features (12)</b> — <i>Click to expand</i></summary>

- **One-tap setup** — bootstrap, Node.js, and OpenClaw installed from within the app
- Built-in dashboard for gateway control, runtime info, and tool management
- **Works independently of Termux** — installing the app does not affect an existing Termux + oa setup
- Android 7.0 or higher (Android 10+ recommended)
- ~1GB free storage
- Wi-Fi or mobile data connection
- ****glibc environment**** — Installs the glibc dynamic linker (via pacman's glibc-runner) so standard Linux binaries run without modification
- ****Node.js (glibc)**** — Downloads official Node.js linux-arm64 and wraps it with an ld.so loader script (no patchelf, which causes segfault on Android)
- ****Path conversion**** — Automatically converts standard Linux paths (/tmp, /bin/sh, /usr/bin/env) to Termux paths
- ****Temp folder setup**** — Configures an accessible temp folder for Android
- ****Service manager bypass**** — Configures normal operation without systemd
- ****OpenCode integration**** — If selected, installs OpenCode using proot + ld.so concatenation for Bun standalone binaries

</details>


---

### 📦 U**niversal Installer

> **Categories:** `#android` `#installer` `#package` `#shizuku`

A modern Android app for installing and managing APK packages with split APK support, silent install via Shizuku, and VirusTotal malware scanning.

- 🐙 **Source Code:** [https://github.com/pass-with-high-score/universal-installer](https://github.com/pass-with-high-score/universal-installer)
- 👤 **Developer:** [pass-with-high-score](https://github.com/pass-with-high-score)

<details>
<summary><b>✨ Key Features (7)</b> — <i>Click to expand</i></summary>

- ***Universal Installer** — The Ultimate Android Package Manager**
- ***Shizuku Integration** — ** Utilize Shizuku for rootless, high-speed background installations.
- ***Automated Scanning** — ** Quickly find and organize all installable packages stored on your device.
- ***Security First** — ** Integrated Malware scanning via VirusTotal API for safer installations.
- ***Smart Cleanup** — ** Automatically delete installation files after a successful install to save storage.
- ***Batch Management** — ** View installation history and manage existing apps from a unified dashboard.
- ***Modern UI** — ** Clean, Material Design interface with intuitive navigation and progress tracking.

</details>


---

### 📦 Secure Screen

> **Categories:** `#Android` `#Security` `#ScreenshotBlocker` `#Privacy`

SecureScreen is a **__NO ROOT__**  Kotlin Android app that prevents screenshots and screen recording for selected apps using FLAG_SECURE-based enforcement.

- 🐙 **Source Code:** [https://github.com/adikul1023/SecureScreen](https://github.com/adikul1023/SecureScreen)
- 👤 **Developer:** [Adi K](https://github.com/adikul1023)

<details>
<summary><b>✨ Key Features (8)</b> — <i>Click to expand</i></summary>

- Select protected apps from installed launchable applications
- Search apps by name or package before enabling protection
- Foreground app detection via UsageStatsManager
- Foreground service with persistent notification
- Transparent SecureActivity enforcement with FLAG_SECURE
- Optional watermark overlay with timestamp and session ID
- Settings for watermark toggle, opacity, and aggressive mode flag
- Boot receiver to recover service state after reboot/update

</details>


---

### 📦 KnoxPatch

> **Categories:** `#Android` `#magisk` `#xposed`

LSPosed module to get Samsung apps/features working again in your rooted Galaxy device.

- 🐙 **Source Code:** [https://telegra.ph/Supported-apps-03-25](https://telegra.ph/Supported-apps-03-25)
- 👤 **Developer:** [salvogiangri](https://github.com/salvogiangri)


---

### 📦 KKND

> **Categories:** `#root` `#android` `#kotlin`

a lightweight Android application that checks whether a device may be rooted or running in a potentially insecure environment.

- 🐙 **Source Code:** [https://github.com/juanma0511/Kknd_Root_Detector](https://github.com/juanma0511/Kknd_Root_Detector)
- 👤 **Developer:** [JUANMA](https://github.com/juanma0511/)

<details>
<summary><b>✨ Key Features (5)</b> — <i>Click to expand</i></summary>

- Detection of su binary in common system paths
- Detection of known root management apps
- Basic system integrity checks
- Detection of suspicious files and directories
- Native‑based detection methods inspired by security research

</details>


---

### 📦 ZKM

> **Categories:** `#Android` `#KernelManager` `#Zkm`

Zuan Kernel Manager App For  Root Device Android With Material 3 Expressive Modern Style.

- 🐙 **Source Code:** [https://github.com/ZUANVFX01/ZKM](https://github.com/ZUANVFX01/ZKM)
- 👤 **Developer:** [ZUANVFX01](https://github.com/ZUANVFX01)

<details>
<summary><b>✨ Key Features (40)</b> — <i>Click to expand</i></summary>

- **Material 3 Expressive Design** - Modern interface with responsive layout and adaptive design
- **LogsView System** - Advanced log reading with dynamic UI components and filtering capabilities
- **Themes & Visual Effects** - Fluid transitions, glassmorphism blur effects (Haze integration), and optimized layouts for various screen densities
- **Enterprise Dashboard** - Real-time monitoring for SoC temperatures, CPU frequencies, and RAM utilization, complete with historical data logging
- **CPU/GPU Tuning** - Comprehensive governor control, min/max frequency management, and boost configuration profiles
- **Memory Management** - LMK (Low Memory Killer) tweaks, virtual memory tuning, ZRAM compression settings, and swap management
- **Thermal & Display Control** - Deep integration with device thermal drivers, brightness curve calibration, and refresh rate management
- **Battery & Doze Optimization** - Wakelock analysis and blocking, charging cycle control, deep sleep optimization, and idle drain prevention
- **Dual-Engine Kernel Flasher** - Flashing system supporting **Horizon Logic** and **Capntrips Architecture** with A/B partition support
- **Secure Terminal Emulator** - Built-in root shell with command history, scripting capabilities, and environment variables management
- **Dex2oat Compiler** - On-device APK optimization for improved runtime performance
- **KsuWebUI Integration** - Embedded WebUI server for KernelSU module management without an external browser
- **System Modding Suite** - Build.prop editor with syntax validation, SetEdit integration for database editing
- **Application Management** - Activity launcher, system app debloating with whitelist protection, and disable/enable controls
- **Real-time Monitoring** - On-screen FPS counter, process resource tracking, and system load monitoring
- ****Operating System**** — Android 10 (Q) or higher
- ****Root Access**** — Magisk v24.0+, KernelSU v0.9+, or APatch
- ****Storage**** — 64MB available space
- ****RAM**** — 2GB minimum (4GB recommended for intensive profiling)
- ****SELinux Status**** — Permissive or Enforcing mode with policy modifications
- ****Bootloader Status**** — Unlocked (required for flasher functionality)
- ****SafetyNet/Play Integrity**** — Bypass required for several advanced features
- *Pre-Installation Check**
- Verify root status via su binary check
- Confirm device architecture compatibility
- *Package Installation**
- Download ZKM-vX.X.X-stable.apk from the [Official Releases](../../releases)
- Enable "Install from Unknown Sources" in device settings
- Execute the installation package
- *Permission Configuration**
- Grant Superuser permissions on first launch
- Allow notifications for real-time monitoring alerts
- Configure storage permissions for backup operations
- Kernel Manager Core Architecture
- CPU/GPU Tuning Engines
- System Monitoring Framework
- Horizon Flasher Logic
- Boot Image Parsing
- Partition Management
- KsuWebUI Standalone Implementation

</details>


---

### 📦 BlockAds

> **Categories:** `#Android` `#AdBlock`

Block ads system-wide on Android using local VPN-based DNS filtering. No root needed. No data collection.

- 🐙 **Source Code:** [https://github.com/pass-with-high-score/blockads-android](https://github.com/pass-with-high-score/blockads-android)
- 👤 **Developer:** [pass-with-high-score](https://github.com/pass-with-high-score)


---

### 📦 StorageFixer

> **Categories:** `#Android` `#Root` `#Xposed` `#Tools`

Fixes Android 16 QPR1+ storage permission bugs on AOSP-based ROMs.

- 🐙 **Source Code:** [https://github.com/omersusin/StorageFixer](https://github.com/omersusin/StorageFixer)
- 👤 **Developer:** [Ömer SÜSİN](https://github.com/omersusin)


---

### 📦 Browser Data Migrator

> **Categories:** `#Android` `#Tools` `#Root` `#Migration`

Browser Data Migrator is a powerful open-source tool designed for power users who want to switch browsers on Android without losing their digital life. Whether you're moving from Firefox to Iceraven or Chrome to Brave, this tool handles the heavy lifting by copying and patching internal database files directly..

- 🐙 **Source Code:** [https://github.com/omersusin/FirefoxTransfer](https://github.com/omersusin/FirefoxTransfer)
- 👤 **Developer:** [omersusin](https://github.com/omersusin)

<details>
<summary><b>✨ Key Features (21)</b> — <i>Click to expand</i></summary>

- ****🚀 One-Tap Migration** — ** Select source and target, press start—done.
- ****📁 Comprehensive Data Support** — ** Moves Bookmarks, History, Cookies, and even Extensions.
- ****🔧 Smart Patching** — ** Automatically updates internal paths and package names within database files (SQLite) and JSON configs.
- ****🛡️ Safety First** — ** Automatic backups are created before any modification.
- ****🧹 Built-in Cleanup** — ** One-tap button to clear migration backups and free up space.
- ****🌍 Wide Compatibility** — ** Supports both **Gecko** (Firefox-based) and **Chromium** (Chrome-based) engines.
- ****Root Access** — ** Essential for reading/writing to /data/data/.
- ****Target Browser Installed** — ** The app you are moving *to* must be installed.
- ****Storage** — ** ~100MB of free space for temporary processing and backups.
- ****Open the App** — ** Grant Root permissions when prompted.
- ****Select Source** — ** Type or paste the package name of your current browser (e.g., org.mozilla.firefox).
- ****Select Target** — ** Type or paste the package name of your new browser (e.g., com.brave.browser).
- ****Start** — ** Tap **START MIGRATION** and watch the real-time log.
- ****Verify** — ** Open your new browser and verify your data is there.
- ****Cleanup** — ** Use **DELETE BACKUPS** to remove the temporary safety copies.
- ****Local Only** — ** No data ever leaves your device. No analytics, no cloud, no internet required.
- ****Input Validation** — ** Strict regex filtering on package names to prevent shell injection.
- ****Sandboxed Execution** — ** Scripts run in a controlled environment under /data/local/tmp.
- ****SELinux Aware** — ** Automatically restores file contexts using restorecon to prevent "App Not Responding" or permission issues.
- ****Chromium Passwords** — ** Due to Android Keystore encryption, passwords moved between different apps (e.g., Chrome -> Brave) may not be decryptable. Migration works best when reinstalling the *same* app or moving within identical signature families.
- ****Tabs** — ** Intentionally skipped to prevent session crashes caused by version mismatches.

</details>


---

### 📦 Blue Light Filter

> **Categories:** `#Android` `#Root` `#Modules`

A module to protect your eyes from harmful blue light directly at the display level, covering every pixel of your screen.

- 🐙 **Source Code:** [https://github.com/NoneBaiano/BlueLightFIlter](https://github.com/NoneBaiano/BlueLightFIlter)
- 👤 **Developer:** [NoneBaiano](https://github.com/NoneBaiano)

<details>
<summary><b>✨ Key Features (6)</b> — <i>Click to expand</i></summary>

- System-wide filter via SurfaceFlinger
- Covers the entire display, including status bar and navigation bar
- Configurable RGB color via built-in WebUI
- No background process. Zero battery impact.
- Auto-start on boot (optional)
- Works with Magisk and KernelSU

</details>


---

### 📦 NothingXpert

> **Categories:** `#Android` `#Nothing` `#Xposed` `#Modules`

A small LSPosed/Xposed module that adds useful features to your Nothing Phone without bloating the system..

- 🐙 **Source Code:** [https://t.me/NothingXpert](https://t.me/NothingXpert)
- 👤 **Developer:** [Rares6567](https://github.com/Rares6567)

<details>
<summary><b>✨ Key Features (18)</b> — <i>Click to expand</i></summary>

- After toggling AMOLED Theme you would have to close and reopen the app
- **Single tap to sleep** — Tap the lock screen to turn the display off
- **Shuffle PIN keypad** — Randomizes the PIN layout every time
- **Double tap to sleep** — Works anywhere (home screen, apps, etc.)
- Lock selected apps with fingerprint or face unlock
- **Screenshot anywhere** — Bypass “secure content” restrictions
- **Shake for flashlight** — Shake the phone (screen off) to toggle torch
- **Volume button actions** — Long-press volume buttons for custom actions
- Nothing OS
- Root access
- LSPosed or another Xposed framework
- Install the APK
- Enable the module in LSPosed
- Activate it for
- System Framework
- SystemUI
- Any app that you add on App Lock
- Reboot

</details>


---

### 📦 Punch-hole Download Progress

> **Categories:** `#Android` `#Xposed` `#Modules` `#Customization`

Xposed module that shows download progress as a ring around the camera cutout.

- 🐙 **Source Code:** [https://github.com/hxreborn/punch-hole-download-progress](https://github.com/hxreborn/punch-hole-download-progress)
- 👤 **Developer:** [hxreborn](https://github.com/hxreborn)

<details>
<summary><b>✨ Key Features (7)</b> — <i>Click to expand</i></summary>

- Progress ring rendered around the camera cutout using the native DisplayCutout API
- **Customizable appearance** — colors per state (active/completed/failed), arc thickness, opacity, and direction
- Completion animations and optional haptic feedback
- Active download counter badge
- Battery saver-aware rendering
- Built-in test mode for simulating states
- Material 3 Expressive settings UI with Jetpack Compose

</details>


---

### 📦 TabletQS

> **Categories:** `#Android` `#XPosed` `#Modules`

Tablet UI style split QS-notification panel on mobile DPI

- 🐙 **Source Code:** [https://github.com/cybr47/TabletSplitQS](https://github.com/cybr47/TabletSplitQS)
- 👤 **Developer:** [Raman](https://github.com/cybr47)


---

### 📦 Kaorios Toolbox

> **Categories:** `#Android` `#Root` `#Shizuku` `#Tools`

Yet a great toolbox for SuperUsers

- 🐙 **Source Code:** [https://github.com/Wuang26/Kaorios-Toolbox](https://github.com/Wuang26/Kaorios-Toolbox)
- 👤 **Developer:** [Kousei](https://github.com/Wuang26/)


---

### 📦 Local Desktop

> **Categories:** `#Android` `#Tools`

Local Desktop is a free, open-source Android application that lets you run a full desktop Linux environment (e.g., a traditional desktop UI such as Xfce) locally on an Android device, without requiring root access.

- 🐙 **Source Code:** [https://github.com/localdesktop/localdesktop](https://github.com/localdesktop/localdesktop)
- 👤 **Developer:** [Local Desktop](https://github.com/localdesktop)


---

### 📦 AppControlX

> **Categories:** `#Android` `#Root` `#Shizuku` `#Tools`

A powerful Android application for controlling app behavior, battery optimization, and system management using Root or Shizuku.

- 🐙 **Source Code:** [https://github.com/risunCode/AppControl-X](https://github.com/risunCode/AppControl-X)
- 👤 **Developer:** [Risun](https://github.com/risunCode)

<details>
<summary><b>✨ Key Features (4)</b> — <i>Click to expand</i></summary>

- App Control
- Battery Optimization
- Tools
- UI/UX

</details>


---

### 📦 BatStats

> **Categories:** `#Android` `#Root` `#Shizuku` `#Tools`

Detailed Stats will not show some of the stats (dependent on device). The app doesn't handle most edge cases, but does almost always work for important ones, like power consumption stats ( in mah ) for all apps.

- 🐙 **Source Code:** [https://github.com/mlm-games/BatStats](https://github.com/mlm-games/BatStats)
- 👤 **Developer:** [ragebreaker](https://github.com/mlm-games)

<details>
<summary><b>✨ Key Features (26)</b> — <i>Click to expand</i></summary>

- Battery monitoring with advanced statistics
- Supports detailed stats via Shizuku (no root required) or root access
- Real-time tracking of battery metrics
- Battery level (%)
- Current draw (mA)
- Voltage
- Temperature
- Power usage
- Configurable sampling/update intervals
- Per-app battery consumption reporting (mAh)
- Enhanced per-app drain analysis using system battery stats (via Shizuku)
- Heuristic-based app drain estimation when enhanced stats are unavailable
- Foreground and usage-based power attribution
- Charging and discharging session tracking
- Session duration tracking
- Average current calculation per session
- Estimated battery capacity calculations
- Detailed battery statistics screen (device-dependent)
- Access to additional system components where supported
- Wakelocks
- Network-related battery usage
- System services consumption
- Expanded and deeper stats on rooted devices
- Availability of detailed stats depends on device, ROM, and Android version
- Some statistics may be missing or incomplete on certain devices
- Advanced features require Shizuku or root permissions

</details>


---

### 📦 AnghamiPlus

> **Categories:** `#Android` `#Music` `#Xposed` `#LSPatch` `#Modules`

AnghamiPlus is a sophisticated Xposed module that enhances your Anghami music streaming experience by unlocking plus-like features directly on the client side. Built with a modular and safe hooking architecture, it provides plus functionality without modifying server behavior or compromising your account security.

- 🐙 **Source Code:** [https://t.me/Kero309x_Chat](https://t.me/Kero309x_Chat)
- 👤 **Developer:** Kero309x

<details>
<summary><b>✨ Key Features (21)</b> — <i>Click to expand</i></summary>

- **🎵 Plus Experience**
- Force plus user checks
- Unlock hidden UI sections
- Enable plus toggles
- **🔄 Unlimited Playback**
- Skip limits removed
- Queue restrictions bypassed
- Related mode forcing disabled
- Player restriction flags patched
- **🚫 Ad-Free Experience**
- Complete ad blocking
- Block popup & banner ads
- *🎤 Karaoke Unlock**
- Unhide karaoke UI elements ( ServerSide Feature )
- **🎛️ Playback Control**
- Disable shuffle mode
- Remove shuffle indicators
- **🎨 UI Enhancements**
- Hide blue header bars
- Remove promo components
- Clean, distraction-free interface

</details>


---

### 📦 Ubuntu Chroot Installer** 😀

> **Categories:** `#Android` `#Root` `#Chroot`

A comprehensive Android Linux environment featuring Ubuntu 24.04 with a built-in WebUI Control Panel, Beautiful desktop environment, advanced namespace isolation, and in-built development tools for a seamless Linux desktop experience on Android - with full hardware access and x86_64 emulation.

- 🐙 **Source Code:** [https://github.com/ravindu644/Ubuntu-Chroot](https://github.com/ravindu644/Ubuntu-Chroot)
- 👤 **Developer:** Ravindu644


---

### 📦 Vanadium WebView & Browser Installer

> **Categories:** `#Android` `#Root` `#Modules`

A Magisk/KernelSU module that changes the system WebView with Vanadium WebView and installs the Vanadium Browser.

- 🐙 **Source Code:** [https://t.me/VanadiumGroup](https://t.me/VanadiumGroup)
- 👤 **Developer:** [NoneBaiano](https://github.com/NoneBaiano)

<details>
<summary><b>✨ Key Features (8)</b> — <i>Click to expand</i></summary>

- Installs Vanadium Trichrome Library
- Installs Vanadium WebView
- Installs Vanadium Browser
- Works with Magisk and KernelSU.
- Automatically debloats conflicting packages.
- Android 10+ (API level 29 or higher)
- Magisk or KernelSU installed
- Internet connection (Wi-Fi recommended)

</details>


---

### 📦 ShizuWall

> **Categories:** `#Android` `#Shizuku` `#Network`

A lightweight, privacy focused Android firewall application that blocks network connections for selected apps without requiring root access or VPN. ShizuWall leverages Shizuku to provide powerful network control capabilities. Requires Android 11 (API 30) or higher.

- 🐙 **Source Code:** [https://github.com/AhmetCanArslan/ShizuWall](https://github.com/AhmetCanArslan/ShizuWall)
- 👤 **Developer:** [Ahmet Can Arslan](https://github.com/AhmetCanArslan)

<details>
<summary><b>✨ Key Features (3)</b> — <i>Click to expand</i></summary>

- **Shizuku-Only Approach** — Most Android firewalls require either Root access or a VPN service. ShizuWall uses only Shizuku, providing native system-level control without the common VPN drawbacks.
- **Per-app System Networking Control** — Uses Android's connectivity service (chain-3) via Shizuku to enable/disable networking on a per-app basis — no packet interception, no VPN tunnel.
- **Privacy-first Design** — The app is offline-first and does not phone home. There is no analytics, no tracking and no telemetry.

</details>


---

### 📦 MovieBox Hooker (XPosed Module)

> **Categories:** `#Android` `#Root` `#Xposed` `#Modules` `#Tools`

MovieBox Hooker is an advanced Xposed Framework module built to unlock VIP and premium features of MovieBox App

- 🐙 **Source Code:** [https://github.com/Kero309x/MovieboxHooker](https://github.com/Kero309x/MovieboxHooker)
- 👤 **Developer:** [Kero309x](https://github.com/Kero309x)


---

### 📦 OnePlus Archive

> **Categories:** `#Android` `#OnePlus` `#Firmware`

OnePlus Archive is a firmware repository for OnePlus phones offering stock OTA images and full firmware packages. It includes archived files for specific partition images to save bandwidth and storage, along with boot/init_boot images for rooting, un-rooting, flashing stock firmware and aftermarket development purposes.

- 🐙 **Source Code:** [https://github.com/spike0en/oneplus_archive](https://github.com/spike0en/oneplus_archive)
- 👤 **Developer:** [Spike](https://github.com/spike0en)


---

### 📦 AppVaultX

> **Categories:** `#Android` `#Root` `#Tools`

AppVaultX is an Android “app vault” that lets you securely store, organize, and quickly launch your important apps from a private dashboard.

- 🐙 **Source Code:** [https://t.me/smartpack_kmanager](https://t.me/smartpack_kmanager)
- 👤 **Developer:** [sunilpaulmathew](https://github.com/sunilpaulmathew)

<details>
<summary><b>✨ Key Features (14)</b> — <i>Click to expand</i></summary>

- Categorizes installed apps as **Recommended**, **Advanced**, **Expert**, or **Unsafe**
- **Powered by trusted data from the [**Universal Android Debloater Next Generation**](https** — //github.com/0x192/universal-android-debloater) project
- ****Force Close Apps**** — safely stop any running app
- ****Clear Data & Cache**** — free storage and reset apps
- ****Backup APKs & Icons**** — save app files and icons for future use
- ****Uninstall Apps (Individual or Batch)**** — remove unwanted apps efficiently
- ****Restore Removed System Apps**** — safely recover system apps
- ****Package Viewer**** — explore installed apps and details
- **▶️ **Open Apps**** — launch any installed app directly
- ****Save APKs & Icons**** — backup apps locally
- ****Access System Settings**** — quick shortcuts to app-related settings
- ****Modern Material Design UI**** — sleek, clean, and intuitive
- ****Batch Operations**** — manage multiple apps effortlessly
- --

</details>


---

### 📦 Jezail

> **Categories:** `#Android` `#Tools`

Jezail is a powerful, all-in-one Android application that runs entirely on your rooted device, transforming it into a comprehensive security testing and device management platform.

- 🐙 **Source Code:** [https://github.com/zahidaz/jezail](https://github.com/zahidaz/jezail)
- 👤 **Developer:** [XAHIDX](https://github.com/zahidaz)


---

### 📦 Restoid

> **Categories:** `#Android` `#Root` `#Tools` `#Backup`

Restoid gives you control over your app backups through a clean and simple user interface. It's built for users who want robust, encrypted, and deduplicated backups.

- 🐙 **Source Code:** [https://github.com/hddq/restoid](https://github.com/hddq/restoid)
- 👤 **Developer:** [hddq](https://github.com/hddq)

<details>
<summary><b>✨ Key Features (8)</b> — <i>Click to expand</i></summary>

- ****Restic-Powered**** — Leverages the speed, security, and efficiency of restic for deduplicated and encrypted backups.
- ****Selective App Backup**** — Choose exactly which user-installed applications you want to back up.
- ****Full Control Over What You Back Up**** — Granularly select what to include for each app: APK files, user data, device-protected data, external/OBB/media files.
- ****Flexible Repository Management**** — Create and manage backup repositories on your device's local storage, SD card, or mounted drives.
- ****Snapshot Management**** — Easily browse backup snapshots, view details of what was backed up, and forget old snapshots.
- ****Flexible Restore**** — Restore entire apps or just specific parts (like only app data).
- ****Downgrade Protection**** — Prevents you from accidentally restoring an older app version over a newer one (can be overridden).
- ****Zero-Hassle Dependencies**** — Automatically downloads and manages the restic binary for your device's architecture.

</details>


---

### 📦 PrivacyFlip

> **Categories:** `#Android` `#Root` `#Privacy` `#Tools`

PrivacyFlip automatically manages your device's privacy features based on lock/unlock state. When you lock your device, it disables Wi-Fi, Bluetooth, mobile data, and location services. When you unlock, it intelligently restores the features you want back on.

- 🐙 **Source Code:** [https://github.com/dorumrr/privacyFlip](https://github.com/dorumrr/privacyFlip)
- 👤 **Developer:** [Doru Moraru](https://github.com/dorumrr)

<details>
<summary><b>✨ Key Features (18)</b> — <i>Click to expand</i></summary>

- **Lock Detection** — Instantly disables selected privacy features when the screen locks
- **Unlock Detection** — Waits for proper authentication (not just screen-on)
- **Smart Restoration** — Re-enable only the features you configured after unlock
- **Wi-Fi** — Toggle wireless connectivity
- **Bluetooth** — Control the Bluetooth radio
- **Mobile data** — Manage cellular data connection
- **Location services** — Toggle GPS and location tracking
- **Lock Delay** — 0–60 seconds before privacy actions are triggered
- **Unlock Delay** — 0–60 seconds before features are restored
- **Instant Mode** — Set delays to 0 for immediate action
- Android 5.0+ (API level 21 or newer)
- Root access (Magisk, SuperSU, etc.)
- Rooted device with su binary available
- **Zero Google Dependencies** — fully F-Droid compliant
- **Pure AndroidX** — modern Android development, no Google services
- **Traditional Android Views** — efficient UI with ViewBinding
- **Navigation Component** — fragment-based navigation
- **MVVM pattern** — reactive architecture with LiveData

</details>


---

### 📦 Volume Key Track Control

> **Categories:** `#Android` `#Xposed` `#Modules` `#Root`

An Xposed module that allows to skip and play/pause track with volume keys

- 🐙 **Source Code:** [https://github.com/Hepolise/VolumeKeyTrackControlModule](https://github.com/Hepolise/VolumeKeyTrackControlModule)
- 👤 **Developer:** [Hepolise](https://github.com/Hepolise)


---

### 📦 Network Switch

> **Categories:** `#installation` `#Android` `#Utilities` `#Network`

A modern Android application that enables users to toggle between 4G and 5G network modes with dual control methods: Root access for rooted devices and Shizuku for non-rooted devices. Built using Jetpack Compose and Material Design 3.

- 🐙 **Source Code:** [https://github.com/aunchagaonkar/NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch)
- 👤 **Developer:** [Ameya Vijay Unchagaonkar](https://github.com/aunchagaonkar)

<details>
<summary><b>✨ Key Features (8)</b> — <i>Click to expand</i></summary>

- Pure network mode switching (LTE-only for 4G, NR-only for 5G)
- Quick Settings tile for instant access
- Dual control methods (Root and Shizuku)
- Modern Material Design 3 interface
- Clean architecture implementation
- Privacy-focused (no internet permissions)
- Intelligent device compatibility detection
- Automatic fallback for unsupported devices

</details>


---

### 📦 HMA-OSS

> **Categories:** `#Android` `#Root` `#XPosed` `#Modules`

An Xposed module to intercept applist and some settings detections.

- 🐙 **Source Code:** [https://github.com/frknkrc44/HMA-OSS](https://github.com/frknkrc44/HMA-OSS)
- 👤 **Developer:** @KaldirimMuhendisi


---

### 📦 Boostify

> **Categories:** `#boostify` `#Android` `#Root` `#XPosed` `#Modules`

Boostify is a modern, Xposed module that supercharges WhatsApp with smart extras, adding advanced features and fine-grained customization and privacy. — inspired by WaEnhancer and MdgWa. It focuses on a clean, preference-first UX, safe guards for power actions, and tools that respect your device.

- 🐙 **Source Code:** [https://github.com/wizdom13/Boostify](https://github.com/wizdom13/Boostify)
- 👤 **Developer:** [wizdom13](https://github.com/wizdom13)


---

### 📦 InstallerX Revived (Community Edition)

> **Categories:** `#key` `#Android` `#Root` `#Utilities`

A modern and functional Android app installer. (You know some birds are not meant to be caged, their feathers are just too bright.)

- 🐙 **Source Code:** [https://github.com/wxxsfxyzm/InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived)
- 👤 **Developer:** [wxxsfxyzm](https://github.com/wxxsfxyzm)


---

### 📦 KonaBess

> **Categories:** `#Android` `#Root` `#Tools`

A GPU overclock & undervolt tool for various Snapdragon chips

- 🐙 **Source Code:** [https://t.me/adreno_konabess](https://t.me/adreno_konabess)
- 👤 **Developer:** [LibXZR](https://github.com/libxzr)


---

### 📦 WhatsMicFix

> **Categories:** `#Android` `#Root` `#Xposed` `#Modules`

Improves the quality and level of audio sent via WhatsApp when the microphone level is lower than expected. Includes an optional 2.00 dB pre-boost (+6.0 dB) .

- 🐙 **Source Code:** [https://github.com/D4vRAM369/WhatsMicFix](https://github.com/D4vRAM369/WhatsMicFix)
- 👤 **Developer:** [D4vRAM369](https://github.com/D4vRAM369)


---

### 📦 Shizuku Package Installer

> **Categories:** `#Android` `#Tools` `#Root`

A lightweight yet powerful package installer for Android.

- 🐙 **Source Code:** [https://github.com/vvb2060/PackageInstaller](https://github.com/vvb2060/PackageInstaller)
- 👤 **Developer:** [南宫雪珊 vvb2060](https://github.com/vvb2060)

<details>
<summary><b>✨ Key Features (15)</b> — <i>Click to expand</i></summary>

- **Split APKs** — Install .apks files generated by bundletool. The installer will selects the most suitable split APKs, mimicking the logic of bundletool install-apks.
- **APK Dumps** — Install apps from zipped APK dumps (a zip file containing all base and split APKs from pm path).
- **Zipped APKs** — Install a single APK from within a ZIP archive.
- **Add Splits** — Add new split APKs to an existing application.
- **Remove Splits** — Remove split APKs from existing application.
- **Interactive Split Installation** — When installing an app that requires splits, user can progressively add more APK files without needing to package them into a single zip file beforehand.
- **Archive Apps** — Archive installed applications to a zip file, which can be used for backup or sharing.
- **Instant Preview** — Quickly view package information without slow copying or temporary extraction.
- **Detailed Info** — Displays the version name, API level, split type and detailed failure reasons.
- **Bypass Play Protect** — Skip the Google Play Protect security scan during installation.
- **Private Space Support** — Handles requests to install applications into Android 15 private space.
- **Default Handler** — Auto set itself as the default app for apk file type.
- **Zero Permissions** — Requires no standard Android permissions.
- **No Background Processes** — Does not spawn any processes.
- **Extremely Small** — The entire app is less than 500KiB in size.

</details>


---

### 📦 SetBox

> **Categories:** `#Android` `#Tools` `#Root`

SetBox is a powerful application that allows you to easily modify Android system settings through community-developed modules.

- 🐙 **Source Code:** [https://github.com/YasserNull/setbox](https://github.com/YasserNull/setbox)
- 👤 **Developer:** [Yasser Null](https://github.com/YasserNull)

<details>
<summary><b>✨ Key Features (3)</b> — <i>Click to expand</i></summary>

- Control settings quickly
- Enable and disable hidden features
- Useful tweaks and some system fixes

</details>


---

### 📦 Shappky

> **Categories:** `#Android` `#Tools` `#Root`

Shappky, short for Shell App Killer, is an app that stops background applications using either Shizuku or Root permissions, improving device performance, reducing memory usage, and lowering heat in a lightweight and safe way.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/9906](https://t.me/popCLOUDS/9906)
- 👤 **Developer:** [Yasser Null](https://github.com/YasserNull)

<details>
<summary><b>✨ Key Features (5)</b> — <i>Click to expand</i></summary>

- **Flexible Permissions** — Works with either Shizuku or Root access.
- **Simplified User Interface** — Practical and easy-to-use design.
- **Fast Performance** — Stops applications with high efficiency.
- **Select System Apps** — Ability to choose system apps for termination.
- **Select Specific Apps** — Choose which apps to stop based on user preference.

</details>


---

### 📦 Infamick

> **Categories:** `#Android` `#Root` `#Modules` `#Optimization`

Infamick is a powerful system utility script for rooted Android devices. It provides easy access to various system information and settings, making it an essential tool for all users.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/9861](https://t.me/popCLOUDS/9861)
- 👤 **Developer:** [Infamousmick](https://github.com/Infamousmick)


---

### 📦 RvKernel Manager

> **Categories:** `#Android` `#Root` `#Tools`

Material Expressive Design Kernel Manager for Android 12+

- 🐙 **Source Code:** [https://github.com/Rve27/RvKernel-Manager](https://github.com/Rve27/RvKernel-Manager)
- 👤 **Developer:** [Radika](https://github.com/Rve27)

<details>
<summary><b>✨ Key Features (5)</b> — <i>Click to expand</i></summary>

- Real-Time Dashboard
- Advanced CPU Control
- GPU Tuning
- **[Github](https** — //github.com/Rve27/RvKernel-Manager/releases)
- **[IzzySoft](https** — //apt.izzysoft.de/fdroid/index/apk/com.rve.rvkernelmanager)

</details>


---

### 📦 AppLock

> **Categories:** `#Android` `#Privacy` `#Security`

AppLock is a modern, open-source Android app locker designed to protect your privacy and sensitive data. Lock any app, prevent unauthorized access, and enjoy a seamless Material You experience. No root required.

- 🐙 **Source Code:** [https://github.com/PranavPurwar/AppLock](https://github.com/PranavPurwar/AppLock)
- 👤 **Developer:** [invoke PranavPurwar](https://github.com/PranavPurwar)

<details>
<summary><b>✨ Key Features (11)</b> — <i>Click to expand</i></summary>

- Material You design, adapts to your theme
- Biometric and PIN authentication
- Anti-uninstall protection
- Unlock timeout for convenience
- No root required
- One-tap app locking
- All data stays on your device
- Real-time background protection
- Lightweight and fast
- **[Github](https** — //github.com/PranavPurwar/AppLock/releases/latest) | [Beta Builds](https://github.com/PranavPurwar/AppLock/raw/refs/heads/master/app/release/app-release.apk)
- **[IzzyOnDroid](https** — //apt.izzysoft.de/packages/dev.pranav.applock)

</details>


---

### 📦 HyperUnlocked

> **Categories:** `#some` `#Android` `#Root` `#Modules` `#Xiaomi`

A Magisk/KernelSU/APatch module made to unlock all high-end features possible to be unlocked on low-end xiaomi devices.

- 🐙 **Source Code:** [https://github.com/ukriu/HyperUnlocked](https://github.com/ukriu/HyperUnlocked)
- 👤 **Developer:** [ukriu](https://github.com/ukriu)


---

### 📦 GPS Rider

> **Categories:** `#Android` `#Xposed` `#Utilities`

GPS Rider is a powerful Android app and Xposed module that allows you to change your device's location system-wide, without enabling Android's mock location setting. This is ideal for testing, automation, privacy, and bypassing apps that detect or block mock locations.

- 🐙 **Source Code:** [https://github.com/dvhamham/gps-rider](https://github.com/dvhamham/gps-rider)
- 👤 **Developer:** [Mohammed Hamham](https://github.com/dvhamham)

<details>
<summary><b>✨ Key Features (12)</b> — <i>Click to expand</i></summary>

- ****System-wide fake location**** — Change your device's location for all apps, without enabling mock location.
- ****Start/Stop/Toggle fake location**** — Control the fake location service easily.
- ****Set custom location**** — Enter latitude and longitude to set any location.
- ****Randomize location**** — Randomize your location within a specified radius for extra privacy.
- ****Set accuracy**** — Control the reported GPS accuracy.
- ****Get current fake location**** — Retrieve the current spoofed coordinates.
- ****Favorites**** — Save and quickly switch between favorite locations.
- ****Material You UI**** — Modern, beautiful, and responsive interface using Jetpack Compose.
- ****Intent API**** — Control the app programmatically from other apps via Intents.
- ****No mock location detection**** — Uses advanced Xposed hooks and anti-detection techniques to hide all traces of mock location.
- ****Multi-process and system service hooks**** — Works at the system level for maximum compatibility.
- ****Root/Xposed required**** — Works with LSPosed/EdXposed.

</details>


---

### 📦 NoWakeLock

> **Categories:** `#Android` `#Root` `#Tools`

NoWakeLock empowers you to take control of your Android device's wakelocks, alarms, and services. By managing how and when apps can wake your device, NoWakeLock helps you significantly reduce power consumption and extend battery life.

- 🐙 **Source Code:** [https://t.me/nowakelock](https://t.me/nowakelock)

<details>
<summary><b>✨ Key Features (9)</b> — <i>Click to expand</i></summary>

- **Wakelock, Alarm & Service Management** — Monitor and block or allow specific wakelocks, alarms, and services on a per-application basis.
- **Material Design 3 UI** — Enjoy a clean, modern, and user-friendly interface.
- **Performance Optimizations** — Benefit from a responsive UI and efficient background processing.
- **Module Status Check** — Easily verify if the Xposed module is active, hooks are working, and configurations are correctly loaded.
- **Regular Expression Support** — Utilize powerful regex patterns for flexible and precise interception rules.
- **Detailed Statistics** — Gain insights into wakelock activity and understand the impact of your configurations.
- **Data Backup & Recovery** — Safeguard your settings and restore them when needed.
- **Boot Reset Functionality** — Ensures data consistency by automatically resetting relevant statistics after a device reboot.
- **Multi-User Support** — Basic support for managing different user profiles on a single device.

</details>


---

### 📦 GooseDroid - Chaos Engine

> **Categories:** `#Android` `#Root` `#Modules`

GooseDroid is a Magisk/KernelSU module that brings random, chaotic, goose-inspired behavior to your Android device for pure entertainment and mischief. Inspired by the spirit of the Desktop Goose, this daemon creates unpredictable disruptions—just because it can.

- 🐙 **Source Code:** [https://github.com/Edxlweiss/GooseDroid](https://github.com/Edxlweiss/GooseDroid)
- 👤 **Developer:** [Edxlweiss](https://github.com/Edxlweiss)


---

### 📦 No need root, you can do with [LSPatch](https://t.me/popMODS/4326) as well or you can use this LSPatch (https://github.com/JingMatrix/LSPatch/releases)

- 🐙 **Source Code:** [https://github.com/JingMatrix/LSPatch](https://github.com/JingMatrix/LSPatch)


---

### 📦 Spotify Plus

> **Categories:** `#Android` `#Root` `#Xposed` `#LsPatch` `#NonRoot`

Spotify Plus is an Xposed module that adds beautiful lyrics to Spotify

- 🐙 **Source Code:** [https://t.me/popCLOUDS/9557](https://t.me/popCLOUDS/9557)

<details>
<summary><b>✨ Key Features (1)</b> — <i>Click to expand</i></summary>

- Beautiful Lyrics!

</details>


---

### 📦 pairipfix

> **Categories:** `#Android` `#Xposed` `#Modules`

This LSPosed module bypasses the "Get this app from Play" screen that appears when installing Android apps as an APK instead of from the Google Play Store.

- 🐙 **Source Code:** [https://github.com/ahmedmani/pairipfix](https://github.com/ahmedmani/pairipfix)
- 👤 **Developer:** [ahmedmani](https://github.com/ahmedmani)


---

### 📦 Bolt Kernel Flasher

> **Categories:** `#Android` `#Root`

Bolt Kernel Flasher is a modern Android application designed to easily flash AnyKernel zips on supported devices. Built entirely with Kotlin, it leverages Material 3 Design and Jetpack Compose for a seamless and intuitive user experience.

- 🐙 **Source Code:** [https://t.me/boltKernelFlasher](https://t.me/boltKernelFlasher)
- 👤 **Developer:** [Trinadh Thatakula](https://github.com/trinadhthatakula)

<details>
<summary><b>✨ Key Features (7)</b> — <i>Click to expand</i></summary>

- Fully reproducible, copylefted libre software (GPLv3.0)
- 100% Kotlin
- Material 3 Design
- Jetpack Compose UI
- Simple and fast kernel flashing
- Supports AnyKernel zips
- Smallest APK size possible (around 1.0 MB)

</details>


---

### 📦 PlusPlusBattery

> **Categories:** `#Android` `#Root`

PlusPlusBattery is a lightweight battery info and health estimation tool specifically tailored for OnePlus/Oppo/Realme devices. It provides real-time monitoring of battery status and can evaluate the Full Charge Capacity (FCC) and the uncompensated raw FCC and State of Health (SOH) of silicon-carbon anode batteries under specific conditions.

- 🐙 **Source Code:** [https://github.com/dijia1124/PlusPlusBattery](https://github.com/dijia1124/PlusPlusBattery)
- 👤 **Developer:** [Runhui Zhou](https://github.com/dijia1124)

<details>
<summary><b>✨ Key Features (14)</b> — <i>Click to expand</i></summary>

- **Real-time Battery Info** — Displays current battery level, voltage, current, charge/discharge power, and health status without root access.
- **Battery Health Estimation** — Calculates and records Full Charge Capacity only when the battery current is 0 and the battery level is 100%. This is used to estimate battery health and lifespan. Not a true value, just an estimation.
- **Cycle Count History** — Records the daily cycle count when the app is opened and saves it locally using a Room database. Users can view this on the history page.
- **Real-Time Battery Monitor Notification** — Posts an ongoing notification showing battery metrics. Info entries can be customized.
- **Root Mode** — Requires root permission to read additional information.
- **Current Remaining Capacity** — Read from /sys/class/oplus_chg/battery/battery_rm. This value changes with battery level.
- **Full Charge Capacity (battery_fcc) (Root Mode)** — Read from /sys/class/oplus_chg/battery/battery_fcc. This value fluctuates based on charging/discharging behavior.
- **Raw Full Charge Capacity (Root Mode)** — Reverse-calculated uncompensated FCC. Silicon-carbon anode batteries typically apply algorithmic compensation based on undervoltage thresholds.
- **Battery Health (battery_soh) (Root Mode)** — Read from /sys/class/oplus_chg/battery/battery_soh. This value fluctuates with usage.
- **Raw Battery Health (Root Mode)** — Reverse-calculated uncompensated SOH. Compensation is usually applied in silicon-carbon batteries based on undervoltage thresholds.
- **Battery Under-voltage Threshold  (vbat_uv) (Root Mode)** — Read from /sys/class/oplus_chg/battery/vbat_uv. The device will shut down if the voltage drops below this threshold.
- **Battery Serial Number (battery_sn) (Root Mode)** — Read from /sys/class/oplus_chg/battery/battery_sn.
- **Battery Manufacture Date (battery_manu_date) (Root Mode)** — Read from /sys/class/oplus_chg/battery/battery_manu_date.
- **Qmax (batt_qmax) (Root Mode)** — Qmax refers to the chemical capacity of the battery. The value of this capacity is load independent. This is the capacity that can be released by a battery under very low load current, usually expressed in mAh. In the system, this value changes triggered by some conditions.

</details>


---

### 📦 HuntGames

> **Categories:** `#Android` `#Root` `#Tools`

HuntGames is an Android memory editor and analysis on ARM64 devices. This project uses the kernel for Read and Write memory.

- 🐙 **Source Code:** [https://t.me/HuntGames77](https://t.me/HuntGames77)
- 👤 **Developer:** [Yervant7](https://github.com/Yervant7)


---

### 📦 Eros Samsung Flasher

> **Categories:** `#Android` `#Samsung` `#Tools`

Eros is a lightweight Android app (3MB) designed to flash firmware on Samsung devices via OTG. No root is required, and it supports all architectures, that is, arm64-v8a, armeabi-v7a, x86, and x86_64. Eros can also run on Android TVs that support the USB Host API.

- 🐙 **Source Code:** [https://t.me/ErosMobileTool](https://t.me/ErosMobileTool)
- 👤 **Developer:** [Gabriel2392](https://github.com/Gabriel2392)

<details>
<summary><b>✨ Key Features (10)</b> — <i>Click to expand</i></summary>

- **Flash tar and tar.md5** — Flash firmware files directly on a connected Samsung device via OTG.
- **Download (Dump) PIT Partition** — Retrieve the device’s PIT partition and save it as a file.
- **Reboot to System** — Reboot the connected device back to the system.
- **MD5 Check** — Checks the integrity of firmware files by verifying their MD5 checksum.
- **Userdata Erase** — Forcefully recreates the device's userdata partition, wiping its data.
- **Repartition** — Recreates the device's (modified) partitions.
- **TFlash Support** — Flash firmware onto the SD card connected to the device, wiping the SD card in the process.
- **Skip MD5 Check** — Optionally skip MD5 verification to speed up the flashing process.
- **AB Partition Support** — Choose which partition to flash on A/B partition devices.
- **Auto Reboot Switches** — Control whether the device reboots automatically after flashing.

</details>


---

### 📦 Biometric Bypass

> **Categories:** `#Android` `#Root` `#Xposed` `#Modules`

This LSPosed (Xposed) module streamlines face unlock by skipping the confirmation step enforced after biometric authentication. It applies the bypass system-wide — so it works across all apps, including banking or security-sensitive ones.

- 🐙 **Source Code:** [https://github.com/rafareborn/biometric-bypass](https://github.com/rafareborn/biometric-bypass)
- 👤 **Developer:** [Rafa Reborn](https://github.com/rafareborn)

<details>
<summary><b>✨ Key Features (2)</b> — <i>Click to expand</i></summary>

- **[Github](https** — //github.com/rafareborn/biometric-bypass/releases)
- **[IzzySoft](https** — //apt.izzysoft.de/fdroid/index/apk/eu.rafareborn.biometricbypass)

</details>


---

### 📦 Bypass WhatsApp **`Unofficial App`** Warning

__Because rooting your device mean you're cooking malware in your basement nowadays.__

⚠️ THE DRAMA:
__"You need the official WhatsApp to login."__
__Yeah, yeah, whatever...__

**📱 METHOD 1: TrickyStore**
- Install [TrickyStore](https://github.com/5ec1cff/TrickyStore/releases/latest) on your root manager
- Reboot
- Edit /data/adb/tricky_store/target.txt and add:
`com.whatsapp`
- (Optional) Install [Tricky-Addon](https://github.com/KOWX712/Tricky-Addon-Update-Target-List) for WebUI
- Optional: Use Valid Keybox from Tricky Add-on
- Clear WhatsApp data/cache

**📱 METHOD 2: WaEnchancer**
- Install [LSPosed](https://github.com/JingMatrix/LSPosed) on your root manager
- Reboot
- Install [WAEnhancer](https://t.me/waenhancher) (.apk)
- Enable WAEnhancer in LSPosed
- Reboot
- Open WAEnhancer → enable Bootloader Spoofer
- Optional: Use a Valid Custom Keybox
- Clear Play Store & WhatsApp data
- Reinstall WhatsApp and log in

**TROUBLESHOOTING:**
- Still showing warnings? Force-close and relaunch WhatsApp
- Persistent issues? You may need basic/device Play Integrity
- Try using a valid keybox, even one that's already revoked
- Clear WhatsApp data again to flush cache
**
NOTE:**
If your ROM is cursed and can't pass BASIC even after spoofing, you've got bigger problems. No module can fake stability. Fix your GMS or flash something sane.

- 🐙 **Source Code:** [https://github.com/KOWX712/Tricky-Addon-Update-Target-List](https://github.com/KOWX712/Tricky-Addon-Update-Target-List)


---

### 📦 ️ How to Pass **Strong Integrity** on Android (Step-by-Step Guide)

This tutorial will help you successfully pass **Basic**, **Device**, and **Strong Integrity** checks in both **Legacy** and **New** Play Integrity responses. Make sure to follow each step carefully.

---

🔧 Step 1: Remove Old Modules

Before starting, **remove any previously installed modules related to Play Integrity Fix** to avoid conflicts.

---

📥 Step 2: Download Required Components

Download the following tools and modules:

- **Zygisk Module** (choose one):
- 🔗 [ReZygisk (Recommended)](https://github.com/PerformanC/ReZygisk)
- 🔗 [NeoZygisk](https://github.com/JingMatrix/NeoZygisk)

- **Play Integrity Module** (choose one):
- 🔗 [PlayIntegrityFix (Recommended)](https://github.com/chiteroman/PlayIntegrityFix)
- 🔗 [PlayIntegrityFork](https://github.com/osm0sis/PlayIntegrityFork)

- **Tricky Tools**:
- 🔗 [TrickyStore](https://github.com/5ec1cff/TrickyStore)
- 🔗 [Tricky Addon – Update Target List](https://github.com/KOWX712/Tricky-Addon-Update-Target-List)

---

⚙️ Step 3: (Optional) Install KSU Web UI

Only if you're **using Magisk**, install one of the following:

- 🔗 [KSU Web UI Standalone](https://github.com/5ec1cff/KsuWebUIStandalone)
- 🔗 [MMRL (alternative)](https://github.com/MMRLApp/MMRL)

---

🔄 Step 4: Reboot Your Device

Once all components are installed, **reboot** your phone to apply the changes.

---

🛠️ Step 5: Configure PlayIntegrityFix

1. Open **PlayIntegrityFix**.
2. Tap **Fetch pif.json** to retrieve the config file.

---

🧩 Step 6: Configure TrickyStore

1. Open **TrickyStore**.
2. Tap the **Action** button (bottom right).
3. Tap the **menu **and select:
- **Select All**
- **Deselect Unnecessary**
- **Set Valid Keybox**

---

📅 Step 7: Set Security Patch Date

1. Tap the **menu** again.
2. Select **Set Security Patch**.
3. Tap **Get Security Patch Date**.
4. Then tap **Save**.

---

🚫 Step 8: Disable ROM Spoofing (Important)

If you're using a **custom ROM**, make sure to **disable any ROM/GMS spoofing options**, as they can interfere with the Play Integrity results.

---

✅ Step 9: Verify Strong Integrity

Use the following app to check your integrity status:

- 🔗 [Play Integrity API Checker](https://play.google.com/store/apps/details?id=gr.nikolasspyr.integritycheck)

If everything was done correctly, you should now pass:

- **Basic Integrity**
- **Device Integrity**
- **Strong Integrity**

For **both legacy and new response formats**.

---

⚠️ Important Note

**Avoid checking Play Integrity too often.**
Only do it when absolutely necessary. Too many checks can make Google suspicious and may cause your device to start failing integrity even if it was previously passing.

---

- 🐙 **Source Code:** [https://github.com/PerformanC/ReZygisk](https://github.com/PerformanC/ReZygisk)


---

### 📦 PixelLauncherEnhanced

> **Categories:** `#Android` `#Customization` `#Xposed` `#Root`

An Xposed module to unleash the full potential of your launcher!!

- 🐙 **Source Code:** [https://github.com/Mahmud0808/PixelLauncherEnhanced](https://github.com/Mahmud0808/PixelLauncherEnhanced)
- 👤 **Developer:** [@DrDisagree](https://github.com/Mahmud0808)

<details>
<summary><b>✨ Key Features (7)</b> — <i>Click to expand</i></summary>

- *
- Double tap to sleep.
- Themed icons for all apps.
- Completely remove at a glance.
- Hide desktop search bar.
- Add clear all button in recents.
- Icon Customizations

</details>


---

### 📦 Oxygen Customizer

> **Categories:** `#Android` `#Root` `#Customization`

Oxygen Customizer is an open-source Android application aimed at providing users with the ability to tweak and customize various aspects of Oxygen OS UI.

- 🐙 **Source Code:** [https://github.com/DHD2280/Oxygen-Customizer](https://github.com/DHD2280/Oxygen-Customizer)
- 👤 **Developer:** Luigi


---

### 📦 GhostGMS

> **Categories:** `#Android` `#Root` `#Modules` `#Optimization` `#Battery` `#Performance`

A universal Magisk module that disables unnecessary GMS background processes, logging, window-level blurs (on MIUI & HyperOS), and tweaks the kernel to optimize performance and battery life.

⚠️ Note:
__May cause issues on stock ROMs like NothingOS (tested) but works fine on MIUI and HyperOS stock ROMs.__

- 🐙 **Source Code:** [https://t.me/veloxineologysupport](https://t.me/veloxineologysupport)
- 👤 **Developer:** [@kaushikieee](https://github.com/veloxineology)

<details>
<summary><b>✨ Key Features (10)</b> — <i>Click to expand</i></summary>

- Disables unnecessary GMS background processes
- Removes extra logging
- Blocks window blurs on MIUI & HyperOS
- Tweaks system for better performance
- Lowers battery drain (10-8% → 4-6%)
- Improves privacy by stopping background activity
- Optimized for custom ROMs (AOSP, CLO, etc.)
- Works on MIUI & HyperOS stock ROMs (issues on NothingOS)
- Fixes location tracking issues
- Code cleanup and bug fixes

</details>


---

### 📦 XPTranslateText

> **Categories:** `#Android` `#Xposed` `#Modules` `#Root`

XPTranslateText is an Xposed module designed to automatically translate text within applications. It prioritizes translations using a local cache, then utilizes the Gemini 2.0 API, and falls back to the free Google API if necessary.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/8683](https://t.me/popCLOUDS/8683)
- 👤 **Developer:** [Tianci Dev](https://github.com/tianci-sh)

<details>
<summary><b>✨ Key Features (3)</b> — <i>Click to expand</i></summary>

- ****Automatic Translation** — ** Seamlessly translates app text without manual intervention.
- ****Multiple Translation Sources** — ** Utilizes a hierarchical approach—first checking local cache, then the Gemini 2.0 API, and finally the free Google API.
- ****Xposed Framework Integration** — ** Requires LSPosed or a similar Xposed Framework variant for functionality.

</details>


---

### 📦 Revanced Xposed

> **Categories:** `#Android` `#Root` `#Xposed` `#Modules`

An Xposed (Lsposed) module, which integrates Revanced patches into YouTube & YouTube music app.

- 🐙 **Source Code:** [https://github.com/chsbuffer/RevancedXposed](https://github.com/chsbuffer/RevancedXposed)
- 👤 **Developer:** [ChsBuffer](https://github.com/chsbuffer)


---

### 📦 System App Nuker

> **Categories:** `#Android` `#Root` `#Tools` `#Debloat` `#Modules`

A simple and efficient module that allows you to remove pre-installed system apps from your Android device

- 🐙 **Source Code:** [https://t.me/systemapp_nuker](https://t.me/systemapp_nuker)
- 👤 **Developer:** [ChiseWaguri](https://github.com/ChiseWaguri)

<details>
<summary><b>✨ Key Features (2)</b> — <i>Click to expand</i></summary>

- **Web-based Interface** — Select apps to remove using a simple WebUI.
- Removing system apps without touching the original partitions.

</details>


---

### 📦 Bootloader Unlock: Wall of Shame

> **Categories:** `#universal` `#Android` `#Utilities`

A list containing phone manufacturers and their policies on unlocking the bootloader. Useful when choosing which phone to buy.

🔗 **Links**
- [The list](https://github.com/melontini/bootloader-unlock-wall-of-shame)
- [SOC based exploits](https://github.com/melontini/bootloader-unlock-wall-of-shame#universal-soc-based-methods)
- [Custom AVB keys](https://github.com/chenxiaolong/avbroot/issues/299)

- 🐙 **Source Code:** [https://github.com/melontini/bootloader-unlock-wall-of-shame](https://github.com/melontini/bootloader-unlock-wall-of-shame)
- 👤 **Developer:** [melontini](https://github.com/melontini)


---

### 📦 Nothing Archive

> **Categories:** `#downloads` `#Android` `#Firmware` `#NothingOS` `#Nothing` `#CMFbyNothing`

A comprehensive collection of unmodified stock firmware images and OTA update links for Nothing and CMF devices, facilitating manual sideloading, rooting, and stock ROM flashing.

- 🐙 **Source Code:** [https://github.com/spike0en/nothing_archive](https://github.com/spike0en/nothing_archive)

<details>
<summary><b>✨ Key Features (6)</b> — <i>Click to expand</i></summary>

- Indexes official OTA update links directly from OEM servers for Nothing and CMF devices.
- Manually sideload updates during region-based rollouts or when the device is unable to install or receive OTA updates.
- Generates stock, unmodified OTA images when full stock firmware is not available from OEM.
- Offers stock boot image files for rooting or unrooting the supported devices.
- Flash official firmware or partition images to resolve boot loops, soft bricks, or revert from custom ROMs.
- Preserves all the available firmware versions for rollback, testing, dumping, or restoration.

</details>


---

### 📦 Thor

> **Categories:** `#Android` `#Root` `#Tools`

Thor is an Android App Manager and App Installer utility

- 🐙 **Source Code:** [https://github.com/trinadhthatakula/Thor](https://github.com/trinadhthatakula/Thor)
- 👤 **Developer:** [Trinadh Thatakula](https://github.com/trinadhthatakula)


---

### 📦 Net Switch: Isolate Apps from Internet Access

> **Categories:** `#Android` `#Modules` `#Root`

Net Switch is a Magisk/KernelSU/APatch module to isolate apps from accessing the internet on your Android device. This module gives you complete control over which apps can send or receive data, improving security, privacy, and saving bandwidth.

- [Download](https://github.com/Rem01Gaming/net-switch/releases/tag/1.0)
- [Source code](https://github.com/Rem01Gaming/net-switch)
- [Support group ](https://t.me/rem01shideout)
- [Update channel ](https://t.me/rem01schannel)

- 🐙 **Source Code:** [https://github.com/Rem01Gaming/net-switch](https://github.com/Rem01Gaming/net-switch)
- 👤 **Developer:** [Rem01Gaming](https://github.com/Rem01Gaming)


---

### 📦 AnyWebView

> **Categories:** `#android` `#root` `#lsposed`

Allows user to switch WebView implementations on any android device.

- 🐙 **Source Code:** [https://github.com/neoblackxt/AnyWebView](https://github.com/neoblackxt/AnyWebView)
- 👤 **Developer:** [neoblackxt](https://github.com/neoblackxt)


---

### 📦 TeleVip (Xposed module)

> **Categories:** `#Android` `#Xposed` `#Root`

A Xposed module for modifying Telegram

- 🐙 **Source Code:** [https://t.me/popCLOUDS/7825](https://t.me/popCLOUDS/7825)
- 👤 **Developer:** [mustafa1dev](https://github.com/mustafa1dev)


---

### 📦 Global Icon Pack

> **Categories:** `#android` `#root` `#xposed`

An Xposed module for applying icon packs globally. Some launchers support icon packs. However the icons are usually not consistent across the whole system.

- 🐙 **Source Code:** [https://github.com/RichardLuo0/global-icon-pack-android](https://github.com/RichardLuo0/global-icon-pack-android)
- 👤 **Developer:** [RichardLuo0](https://github.com/RichardLuo0)


---

### 📦 Screenshot Tile No Root

> **Categories:** `#Android` `#Screenshot`

This is a tools to take screenshot without root by using accessibility services

- 🐙 **Source Code:** [https://github.com/cvzi/ScreenshotTile](https://github.com/cvzi/ScreenshotTile)
- 👤 **Developer:** [cvzi](https://github.com/cvzi)

<details>
<summary><b>✨ Key Features (3)</b> — <i>Click to expand</i></summary>

- take screenshot using Accessibility services or screen capturing permission
- open source
- only have necessary permission to perform it's intended function

</details>


---

### 📦 Cleaner Royall: The Most Advanced Root Cleaner for Android

> **Categories:** `#Android` `#Utilities` `#Cleaner` `#Performance`

The best cleaning app ever made—ultra-fast, lightweight, and powerful. Root or Magisk & Busybox only. No permissions needed (except root), no data collection, and includes an automatic cleaner module.

- 🐙 **Source Code:** [https://github.com/araafroyall/Cleaner-Royall](https://github.com/araafroyall/Cleaner-Royall)
- 👤 **Developer:** [GitHub @AraafRoyall](https://github.com/araafroyall)


---

### 📦 Frosty

> **Categories:** `#Android` `#iOS` `#Social` `#Root` `#Modules`

A mobile Twitch client for iOS and Android with 7TV, BetterTTV (BTTV), and FrankerFaceZ (FFZ) support.

- 🐙 **Source Code:** [https://github.com/tommyxchow/frosty](https://github.com/tommyxchow/frosty)
- 👤 **Developer:** [Drsexo](https://github.com/Drsexo)

<details>
<summary><b>✨ Key Features (37)</b> — <i>Click to expand</i></summary>

- Support for 7TV, BetterTTV, and FrankerFaceZ emotes and badges
- Browse followed streams, top streams, and top categories
- Autocomplete for emotes and user mentions
- Light, dark, and black (OLED) themes
- Search for channels and categories
- See and filter chatters in a channel
- Local chat user message history
- Theater and fullscreen mode
- Watch live streams with chat
- Picture-in-picture mode
- Block and report users
- Emote menu
- Sleep timer
- **Telemetry** - Ads, analytics, tracking (safe to disable)
- **Background** - Updates, background sync (safe to disable)
- **Location** - GPS, geofencing, activity recognition
- **Connectivity** - Chromecast, Quick Share, Nearby
- **Cloud** - Backup, sync, authentication
- **Payments** - Google Pay, Wallet, NFC
- **Wearables** - Wear OS, Google Fit
- **Games** - Play Games achievements, cloud saves
- **XML Patching** - Removes GMS from power-save whitelists
- **DeviceIdle Integration** - Allows Android Doze to optimize GMS
- **Conflict Resolution** - Patches other modules that whitelist GMS
- **Toggleable** - Enable/disable with the action button
- **Deep Sleep Enforcement** - Forces the device into deep sleep immediately when the screen locks.
- **Background Restrictions** - Blocks apps from running in the background to stop battery-draining loops.
- **WAKE_LOCK Denial** - Denies WAKE_LOCK permissions to block useless CPU-heavy wakelocks.
- **Kernel Tweaks** - Scheduler, VM, and network optimizations
- **Blur Disable** - Reduce GPU load by disabling UI blur effects
- **Log Killing** - Stop battery-draining log processes (logcat, traced, etc.)
- **Empty RC Files** - Overlay system init scripts to prevent debug daemons
- **Volume Key Selection** - Easy installation choices
- **Action Button Toggle** - Switch modes from root manager
- **Comprehensive Logs** - Detailed logs in /data/adb/modules/Frosty/logs/
- **Status Report** - Quick status check via terminal
- **Clean Uninstall** - Complete reversal of all changes

</details>


---

### 📦 AnLinux

> **Categories:** `#Android` `#Linux` `#Tools`

Run Linux on Android without root access. Supports 2 Desktop Environments, and only [Ubuntu](https://www.ubuntu.com/), [Debian](https://www.debian.org/), [Kali](https://www.kali.org/), [Parrot Security OS](https://www.parrotsec.org/), [Fedora](https://getfedora.org/) distros are supported.

- 🐙 **Source Code:** [https://github.com/EXALAB/AnLinux-Adfree](https://github.com/EXALAB/AnLinux-Adfree)


---

### 📦 MultiLocale

> **Categories:** `#Android` `#Root`

A simple app that enables you to add additional (or "unsupported") languages to your device's locale settings, if the OEM (__ahem__ Xiaomi) doesn't let you.

❗Requirements:
- Android 7.0 (SDK 24) or more.
-Shizuku/root or ADB to grant one of the needed permissions for changing the device's locale settings (android.permission.CHANGE_CONFIGURATION).

- 🐙 **Source Code:** [https://t.me/popCLOUDS/6843](https://t.me/popCLOUDS/6843)


---

### 📦 Timed Shutdown Android app (No Root)

> **Categories:** `#Android` `#Utilities`

An app for android that will automatically shutdown your phone after a timer without needing root access. This app uses the accessiblity permission to emulate the power off gestures.

- 🐙 **Source Code:** [https://github.com/maforn/TimedShutdownAndroid](https://github.com/maforn/TimedShutdownAndroid)


---

### 📦 MemLoader (formerly XLoad)

> **Categories:** `#notes` `#credits` `#Android` `#Root` `#Modules`

Load objects directly into RAM to reduce I/O operations and improve access speed.

- 🐙 **Source Code:** [https://github.com/iamlooper/MemLoader](https://github.com/iamlooper/MemLoader)


---

### 📦 dex2oat optimizer

> **Categories:** `#notes` `#credits` `#Android` `#Root` `#Modules`

An ART optimization module to accelerate app launches and improve system performance.

- 🐙 **Source Code:** [https://github.com/iamlooper/dex2oat-optimizer](https://github.com/iamlooper/dex2oat-optimizer)


---

### 📦 MemeUI Enhancer

> **Categories:** `#notes` `#credits` `#Android` `#Root` `#Modules`

Enhances MIUI/HyperOS for better battery backup and performance.

- 🐙 **Source Code:** [https://github.com/iamlooper/MemeUI-Enhancer](https://github.com/iamlooper/MemeUI-Enhancer)


---

### 📦 Cirno

> **Categories:** `#Android` `#XPosed` `#Modules` `#Root`

Cirno is an application freezer that runs on all platforms with Android 12+ to completely prevent background applications from using CPU resources, thereby improving the overall smoothness of the device.Cirno is currently only supported on cgroup v2 devices, which means your Linux kernel version needs to be greater than or equal to 5.0. The app has no GUI. It will freeze apps automatically. By modifying the cfg file, you can specify that the application does not freeze.

- 🐙 **Source Code:** [https://apt.izzysoft.de/fdroid/index/apk/nep.timeline.cirno](https://apt.izzysoft.de/fdroid/index/apk/nep.timeline.cirno)


---

### 📦 BCL and ACC

> **Categories:** `#Android` `#Root` `#Modules`

**ACC** is an Android software mainly intended for extending battery service life. In a nutshell, this is achieved through limiting charging current, temperature and voltage. Any root solution is supported. Regardless of whether the system is rooted with KernelSU/Magisk, the installation is always "systemless".

**BatteryChargeLimit** is an Android application designed to help users manage their device's battery charging process. By setting a desired charge limit, the app prevents the battery from charging beyond a specified percentage, which can help prolong battery life and maintain its health.

- 🐙 **Source Code:** [https://github.com/VR-25/acc](https://github.com/VR-25/acc)


---

### 📦 Re-Malwack

> **Categories:** `#Android` `#Magisk` `#module` `#ad_block` `#adblock` `#ad_blocker` `#adblocker`

A revival of Malwack magisk module, yet it is also updated regularly and enhanced :)

🛠️ Features

• Hosts file updated regularly
• No need to update module to get updated hosts file, you can update it by a small command :)
• Ability to add links to the block list easily
• Gets rid of ads and malware.
• Gets rid of p*rn stuff (optional XD)
• Ensures security to your device
• Doesn't affect device performance
• Ability to reset hosts file to default

🔗Links
- [Download](https://github.com/ZG089/Re-Malwack/releases/latest)
- [Source Code](https://github.com/ZG089/Re-Malwack)
- [XDA Support thread](https://xdaforums.com/t/re-malwack-revival-of-malwack-module.4690049/)
- [Donate to the developer](https://buymeacoffee.com/zg089)

🌐 @popmodsnetwork
🎁 [Donate to our admins](https://t.me/popCLOUDS/6339)

- 🐙 **Source Code:** [https://github.com/ZG089/Re-Malwack](https://github.com/ZG089/Re-Malwack)


---

### 📦 Pixelspoof

> **Categories:** `#Android` `#xposed` `#root`

A module for LSPosed that lets you spoof all device-specific properties of your device, selectively for individual apps.

✳️Benefits:
• Enables magic editor for Google Phhotos
• Get free 6 months subscription on Google One
• Easily spoof your device model for any apps
• more...

- 🐙 **Source Code:** [https://github.com/RisenID/PixelSpoof](https://github.com/RisenID/PixelSpoof)


---

### 📦 Pixel Studio Enabler

> **Categories:** `#Android` `#xposed` `#root`

Enables Pixel Studio App for all devices (A13+) systemlessly.

__**Pixel Studio** uses state-of-the-art generative AI to create unique and fun images on your Pixel.__

✳️ Here’s what you can do:
● Enter a description and Pixel will create it, or upload your own image
● Add stickers
● Add captions in different fonts and colors
● Remove or move items with gestures
● Save projects
• Admire the beautiful UI.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/6339](https://t.me/popCLOUDS/6339)


---

### 📦 Smart Pixels (XPosed Module)

> **Categories:** `#Android` `#Xposed` `#Modules` `#Root`

Smart Pixels is a battery-saving function found on some devices. It works by turning off certain pixels on the screen to reduce power consumption. This can be particularly useful for extending battery life without significantly impacting the display quality.

- 🐙 **Source Code:** [https://github.com/frknkrc44/SmartPiXelsPosed](https://github.com/frknkrc44/SmartPiXelsPosed)


---

### 📦 Keyboard GPT

> **Categories:** `#Android` `#Root` `#NoRoot` `#LSPosed`

**
An LSPosed Module that lets you integrate Generative AI like ChatGPT into your own keyboard.

**Supported-**
[ChatGPT](https://chatgpt.com/)
[Gemini](https://gemini.google.com/?hl=en-IN)

Api-
[ChatGpt](https://platform.openai.com/api-keys) (paid)
[Gemini](https://ai.google.dev/) (free)

🔗 **Links**:
- [Download](https://github.com/Mino260806/KeyboardGPT/releases/)
- [XDA](https://xdaforums.com/t/mod-xposed-integrate-generative-ai-like-chatgpt-in-keyboard.4683421/)
- [Demo](https://t.me/popCLOUDS/6135)
- [Installation](https://t.me/popCLOUDS/6136)
- [Support Dev](https://buymeacoffee.com/androidmaestro)
- [SourceCode](https://github.com/Mino260806/KeyboardGPT)
- Thanks to @XposedRepository for sharing it

🌐 @popmodsnetwork
🎁 [Donate to our admins](https://t.me/popMODS/4195)

- 🐙 **Source Code:** [https://github.com/Mino260806/KeyboardGPT](https://github.com/Mino260806/KeyboardGPT)


---

### 📦 NLSound

> **Categories:** `#Android` `#Magisk` `#KSU`

**
This module allows you to enchance your audio quality with a lot of settings in it

- 🐙 **Source Code:** [https://github.com/Briclyaz/NLSound_module_QCom](https://github.com/Briclyaz/NLSound_module_QCom)


---

### 📦 WhatsApp MaterialYou Guide!

__Use material you colors in WhatsApp__ [ROOT REQUIRED]

**✅ Prerequisites:**
- Rooted android device.
- LSPosed framework ([GitHub](https://github.com/mywalkb/LSPosed_mod))
- Latest WA Enhancer module ([GitHub](https://github.com/Dev4Mod/WaEnhancer), [TG](https://t.me/waenhancher))

**📝 Procedure:** ([Screenshots](https://t.me/MaterialYouStuff/245?single))
1. Install and setup prerequisites.
2. Head over to __"Customisation"__ menu in WA Enhancer.
3. Make sure __"Colors"__ is enabled and __"Customize your colors"__ is disabled.
4. Download this file: [Material You.zip](https://t.me/waenhancher/131)
5. Import the .zip file into __"Theme Manager".__
6. Restart WhatsApp and Profit!!1!1!

**🖼️ Screenshots:** [**Check Here!**](https://t.me/MaterialYouStuff/252?single)
**
💬 Join:**
- @MaterialYouApps
- @MaterialYouAppsChat

- 🐙 **Source Code:** [https://github.com/mywalkb/LSPosed_mod](https://github.com/mywalkb/LSPosed_mod)


---

### 📦 Tarnhelm - The magic to clean sharing links up.

> **Categories:** `#Android` `#Xposed` `#Modules`

Tarnhelm can help you clean the tracking parameters in the links shared from the apps and keep the process natural.

- 🐙 **Source Code:** [https://play.google.com/store/apps/details?id=cn.ac.lz233.tarnhelm](https://play.google.com/store/apps/details?id=cn.ac.lz233.tarnhelm)


---

### 📦 DataBackup

> **Categories:** `#support` `#Android` `#Root`

DataBackup is a rooted app that allows you to back up your apps, folders/files, Wi-Fi networks, calls, and messages (Wi-Fi, calls, and messages are not implemented yet, we are working on it) to a local and/or your server.

- 🐙 **Source Code:** [https://apt.izzysoft.de/fdroid/index/apk/com.xayah.databackup](https://apt.izzysoft.de/fdroid/index/apk/com.xayah.databackup)

<details>
<summary><b>✨ Key Features (6)</b> — <i>Click to expand</i></summary>

- Multi-user Support
- Cloud
- 100% Data Integrity
- Fast
- Easy
- Monet Theme

</details>


---

### 📦 WifiList (FOSS)

> **Categories:** `#Android`

View your saved WiFi passwords on Android 11 and later without root!

WiFiList is (almost) fully open source. Feel free to browse the code to confirm security.

Aside from crash reports, zero data is collected and there is zero internet connectivity. Your passwords remain on your device.

- 🐙 **Source Code:** [https://github.com/jaredcat/WiFiList](https://github.com/jaredcat/WiFiList)


---

### 📦 Pi Installer

> **Categories:** `#Android`

is short for "Package Installer". It is just a Package Installer and its function is very simple. In short, my idea is, this app works for me, you can use it if you like, but if you need features that I don't need, then I won't add them. It's just a niche project.

PI requires Shizuku or root to acquire the elevated privileges needed to do its job.

- 🐙 **Source Code:** [https://github.com/SanmerApps/PI](https://github.com/SanmerApps/PI)


---

### 📦 MMRL

> **Categories:** `#Android` `#Root`

MMRL is a highly configurable app allows you to manage modules effortlessly, all while being completely free of ads.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/5510](https://t.me/popCLOUDS/5510)


---

### 📦 Yet Another Mi-FreeForm** **(Squared)

> **Categories:** `#Android` `#Xposed` `#Modules`

Yet Another Mi-FreeForm is a fork of famous Mi-FreeForm Xposed module

- 🐙 **Source Code:** [https://github.com/kaii-lb/YAMFsquared](https://github.com/kaii-lb/YAMFsquared)


---

### 📦 USB HID Client

> **Categories:** `#Android` `#Root`

Android app that allows you to easily use your phone as a keyboard, mouse WITHOUT any software on the other end.

🔗 **Links**:
- Download From [Github](https://github.com/Arian04/android-hid-client/releases/) or [IzzyDroid](https://apt.izzysoft.de/fdroid/repo/me.arianb.usb_hid_client_220.apk)
- [Screenshots](https://t.me/popCLOUDS/5205)
- [SourceCode](https://github.com/Arian04/android-hid-client/releases/)

🌐 @popmodsnetwork
🎁 [Donate to our admins](https://t.me/popMODS/4195)

- 🐙 **Source Code:** [https://t.me/popCLOUDS/5205](https://t.me/popCLOUDS/5205)


---

### 📦 AppErrorsTracking

> **Categories:** `#Android` `#SuperUser` `#Xposed`

AppErrorsTracking is a Xposed Module tailored for Android developers. It enhances error handling by capturing app errors, useful when ADB is not an option. This module replaces the system's error dialog, offering features like exception logging, copying, sharing, exporting stack traces, and maintaining an error history.

🔗 **Quick Access**;
- Try It Out: [Stable](https://github.com/KitsunePie/AppErrorsTracking/releases), [CI builds](https://t.me/AppErrorsTracking_CI)
- Gallery: [Screenshots](https://t.me/fossclouds/83)
- Learn More: [Features](https://t.me/fossclouds/82), [Github Repo](https://github.com/KitsunePie/AppErrorsTracking)

❤️ Don't forget: If you like it and find it useful, you can support the developer by giving the software a star in the repository/release market, donating or following the developer.

🗨 **Let's Talk**: @fosspalchat

🏷 **Tags**: #Android #SuperUser #Xposed

- 🐙 **Source Code:** [https://t.me/fossclouds/83](https://t.me/fossclouds/83)


---

### 📦 Auto Airplane Mode

> **Categories:** `#Android` `#Root` `#ADB`

Schedule airplane mode based on your settings, e.g. by date/time.
**Root access is required to write secure system settings!**

🔗 **Links**:
- Download from [F-Droid](https://f-droid.org/packages/org.miamplayer.autoairplanemode/) or [Github](https://github.com/MBach/AutoAirplaneMode)
- [Screenshots](https://t.me/popCLOUDS/5053)
- [Source Code](https://github.com/MBach/AutoAirplaneMode)

🌐 @popmodsnetwork
🎁 [Donate to our admins](https://t.me/popMODS/4195)

- 🐙 **Source Code:** [https://github.com/MBach/AutoAirplaneMode](https://github.com/MBach/AutoAirplaneMode)


---

### 📦 AppLaunch

> **Categories:** `#Android` `#Root`

AppLaunch is Alpha-stage project which aims to allow user launch apps from Termux. For example if your home app is Termux.

- 🐙 **Source Code:** [https://github.com/fluid-developer/AppLaunch](https://github.com/fluid-developer/AppLaunch)
- 👤 **Developer:** [releases/latest
-](https://t.me/popMODS/4195)

<details>
<summary><b>🖼️ Preview Screenshots & Media (1)</b> — <i>Click to view images & decide if you want to use this app</i></summary>

#### 📸 Cover / Preview
<p align="center"><img src="../../assets/apps/applaunch/cover.jpg" alt="Cover / Preview" style="max-height: 480px; max-width: 100%; border-radius: 8px; margin: 8px auto;" /></p>

</details>


---

### 📦 Sui

> **Categories:** `#Android` `#Root`

Sui provides Java APIs, [Shizuku API](https://github.com/RikkaApps/Shizuku-API), for root apps. It mainly provides the ability to use Android APIs directly (almost in Java as the identity of the root, and start app's own AIDL-style Java service under root. This will make root app development much more comfortable.

- 🐙 **Source Code:** [https://github.com/RikkaApps/Shizuku-API](https://github.com/RikkaApps/Shizuku-API)


---

### 📦 Neo-Wellbeing** **[Alpha]

> **Categories:** `#android` `#root` `#module`

Open source "Digital Wellbeing" replacement at alpha stage. Has some cool features like Grayscale, Focus mode, Sleep mode, Auto aeroplane mode and so many things.

- 🐙 **Source Code:** [https://github.com/NeoApplications/Neo-Wellbeing](https://github.com/NeoApplications/Neo-Wellbeing)


---

### 📦 Comatose

> **Categories:** `#android` `#root` `#adb`

Force your device to enter deep sleep sooner

Note that this app requires the WRITE_SECURE_SETTINGS permission that can be granted with EITHER a PC using ADB or root. Root is NOT required for this app, it is optional. Android 8.0+ is supported, with more features enabled on Android 10+.

Uninstalling the app will not reset the device configuration. You must click the Reset button to undo all changes made by Buoy.

- 🐙 **Source Code:** [https://github.com/tytydraco/Comatose](https://github.com/tytydraco/Comatose)


---

### 📦 Securify

> **Categories:** `#Android`

Yet another detection app to detect Magisk or KernelSU.

- 🐙 **Source Code:** [https://github.com/RabahX/Securify](https://github.com/RabahX/Securify)


---

### 📦 JamesDSP

> **Categories:** `#features` `#Android` `#Root`

Cross-platform Audio Effect / Digital Signal Processing library

- 🐙 **Source Code:** [https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp&utm_source=github&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1)


---

### 📦 POW

> **Categories:** `#Android` `#ADB` `#Root`

Say hello to Purr, the all-in-one resolution changer for Android devices, no root required! How does it work you ask? We use Android SDK reflection to access hidden APIs to change the resolution of your phone screen. All we need is a special permission that can be granted using ADB.

- 🐙 **Source Code:** [https://play.google.com/store/apps/details?id=com.draco.purr](https://play.google.com/store/apps/details?id=com.draco.purr)


---

### 📦 MdgWa** (Neko xD)

> **Categories:** `#Android` `#Root` `#Lsposed`

An Xposed module to customize your WhatsApp.

- 🐙 **Source Code:** [https://github.com/ItsMadruga/MdgWa](https://github.com/ItsMadruga/MdgWa)


---

### 📦 SimpleAppDowngrader [ROOT]

> **Categories:** `#Android`

Downgrades installed apps with an apk-file

This uses androids pm tool to downgrade already installed apps to an older version.
Root access is required.

- 🐙 **Source Code:** [https://github.com/GaryOderNichts/SimpleAppDowngrader](https://github.com/GaryOderNichts/SimpleAppDowngrader)


---

### 📦 QtScrcpy

> **Categories:** `#Windows` `#Linux` `#MacOS`

QtScrcpy supports displaying and controlling Android devices via USB or over network. It does NOT require root privileges.

- 🐙 **Source Code:** [https://github.com/barry-ran/QtScrcpy](https://github.com/barry-ran/QtScrcpy)


---

### 📦 Geto

> **Categories:** `#installation` `#Android` `#Root`

Apply custom settings to your apps

- 🐙 **Source Code:** [https://t.me/popCLOUDS/4237](https://t.me/popCLOUDS/4237)


---

### 📦 AlternativeUnlockXposed

> **Categories:** `#Android` `#Root` `#Lsposed`

This app provides an reliable way to run something when providing a specific, wrong PIN on your Android lock screen.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/4219?single](https://t.me/popCLOUDS/4219?single)


---

### 📦 Install with options

> **Categories:** `#Android` `#ADB` `#Shizuku`

An app with a simple purpose: more advanced app installs without needing to use ADB

- 🐙 **Source Code:** [https://github.com/zacharee/InstallWithOptions](https://github.com/zacharee/InstallWithOptions)


---

### 📦 Material You redesign of **[**aShell**](https://t.me/popMODS/3182)

> **Categories:** `#Android` `#ADB` `#Shizuku`

You remember [aShell](https://t.me/popMODS/3182)? yeah, aShell is a way for executing commands in the adb shell through shizuku, which let you save and search the command outputs.

But it was not md3.

So an awesome dev, [Hridayan](https://github.com/DP-Hridayan), made an md3 redesign of the app.

- 🐙 **Source Code:** [https://github.com/DP-Hridayan/ashell](https://github.com/DP-Hridayan/ashell)


---

### 📦 AdClose

> **Categories:** `#Android` `#Root` `#Modules`

AdClose is an Android ad-blocking tool based on the Xposed framework. It aims to provide a **no-ad** app browsing experience, optimize user experience and reduce interference. It is recommended to use it in the LSPosed framework environment. AdClose's core function is to prevent the initialization and loading of ad SDKs in apps, and intercept app ad requests to block ads.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/4089](https://t.me/popCLOUDS/4089)

<details>
<summary><b>✨ Key Features (6)</b> — <i>Click to expand</i></summary>

- **Accurate processing** — Prevent the initialization of ad SDKs in apps.
- **Ad request interception** — Block ad requests in apps.
- **Screenshot and screen recording restriction removal** — Allow free screenshot and screen recording in apps.
- **VPN and proxy detection removal** — Remove VPN and system proxy detection in apps.
- **Sensor listening removal** — Disable sensor-based ad jumps such as shake.
- **Root detection evasion** — Remove general Root, Magisk and Xposed framework detection in apps.

</details>


---

### 📦 ️**APatch** - Android Kernel and System Patcher

> **Categories:** `#Android` `#Root` `#Magisk` `#Modules`

APatch is an application that allows the modification of the Android kernel and system. This application provides support for the Root APM module, similar to Magisk, and the Kernel Patch Module (KPM), which allows for any code to be injected into the kernel.

- 🐙 **Source Code:** [https://github.com/bmax121/APatch](https://github.com/bmax121/APatch)


---

### 📦 A1Memory Management

> **Categories:** `#important` `#custom` `#terminal` `#frequently` `#default` `#Android` `#Root` `#Modules`

A1Memory is a memory management module for Android devices that optimizes the performance and battery life of your applications. It runs on Magisk and ksu, and it supports Android 8 to 14 and till 15. It allows you to control the background processes, the low memory killer daemon, and the memory release of your applications. It also provides a terminal UI and a JSON configuration file for customization.

- 🐙 **Source Code:** [https://github.com/OneB1ank/A1Memory](https://github.com/OneB1ank/A1Memory)


---

### 📦 Android Enhancer | Revolutionary Android Optimizer

> **Categories:** `#screenshots` `#download` `#credits` `#Android` `#Root` `#Modules`

Android Enhancer is a specialized tool designed to optimize the performance of Android devices by modifying specific core parameters. Unlike other optimizers, Android Enhancer employs a universal approach, enabling it to function effectively across a wide range of Android devices. Consequently, it can enhance the performance of various devices, encompassing smartphones, tablets, and other Android-powered devices.

- 🐙 **Source Code:** [https://github.com/iamlooper/Android-Enhancer](https://github.com/iamlooper/Android-Enhancer)
- 👤 **Developer:** [iamlooper](https://github.com/iamlooper)


---

### 📦 PlayIntegrityFix & PlayIntegrityFixNext

> **Categories:** `#Android` `#Root` `#Modules`

**
PlayIntegrityFix is a Magisk module that aims to fix Play Integrity and SafetyNet verdicts on rooted Android devices with unlocked bootloaders. It works by injecting into Google Play Services and preventing it from using hardware attestation, as well as spoofing a low Android fingerprint. This way, it can bypass the latest Google Play Protect checks and make your device appear as certified.

- 🐙 **Source Code:** [https://t.me/playintegrityfix](https://t.me/playintegrityfix)


---

### 📦 Disable Target API Block

> **Categories:** `#Android` `#Root` `#Modules`

**
An Xposed module for disabling Android 14's installation block for old apps

- 🐙 **Source Code:** [https://github.com/buttercookie42/DisableTargetAPIBlock](https://github.com/buttercookie42/DisableTargetAPIBlock)


---

### 📦 The detectability of LSPosed by third-party apps raises privacy and security concerns, reflecting unprofessionalism. This issue arises as developers created a native detection project, removed it later, and witnessed the emergence of forks of the original project. Unfortunately, my attempts to address this matter led to expulsion and a ban from their group. Advocating against this unfair and unprofessional practice is crucial, emphasizing its implications for privacy and security. (Kindly refrain from using vulgar language.)

[Anti Magisk & Xposed by LSPosed dev canyie ](https://blog.canyie.top/2021/05/01/anti-magisk-xposed/)([Translated by HuskyDG](https://huskydg.github.io/blog/detect_magisk_xposed.html))
[XposedDetector](https://github.com/xfqwdsj/XposedDetector)

John Wu rebbutal: [1.](https://t.me/CodeOfMeowCat/231473) [2.](https://t.me/CodeOfMeowCat/231491) [3.](https://t.me/CodeOfMeowCat/231498) [4.](https://t.me/CodeOfMeowCat/231509)
MlgmXyysd rebbutal: [1.](https://t.me/AndroidRepo_chat/74679) [2.](https://t.me/op9discussion/106509)

[SilmVXposed & SPatch describe how LSPosed killed its upstream project](https://xdaforums.com/t/something-about-lsposed.4236335/post-85007847)

They even go to other peoples repositories to spam in order to promote their projects https://github.com/MlgmXyysd/kernel-assisted-superuser/pull/1

There are also countless Xposed modules that vanished from the WWW as they don't want it to exist.
([The module in question](https://t.me/HookVipChat/213698))

- 🐙 **Source Code:** [https://github.com/xfqwdsj/XposedDetector](https://github.com/xfqwdsj/XposedDetector)


---

### 📦 🎨 ColorBlendr

> **Categories:** `#Android` `#Root` `#Modules`

An Xposed module to modify material you colors on your device.
Elevate your creativity with effortless material customization. Instantly tweak colors for a personalized touch in just a few taps.

🛠️ **Features **
- Accent saturation changer
- Background saturation changer
- Background lightness changer
- Pitch black theme in dark mode
- Follows wallpaper color
- and many more to come...

- 🐙 **Source Code:** [https://t.me/IconifyDiscussion](https://t.me/IconifyDiscussion)


---

### 📦 [Universal GMS Doze 1.9.1 released](https://t.me/popCLOUDS/3134)

Changelog:
- Improved installation (Magisk Live and KernelSU)
- Fixed root method detections
- Fixed uninstaller script
[source code](https://github.com/gloeyisk/universal-gms-doze)

- 🐙 **Source Code:** [https://github.com/gloeyisk/universal-gms-doze](https://github.com/gloeyisk/universal-gms-doze)


---

### 📦 Tool Shells

> **Categories:** `#Android`

Is an application to edit the apk.
Support to install apk files, apks, apkm, xapk etc. Also can run with root and non-root.

- 🐙 **Source Code:** [https://github.com/kakathic/Tool-Shells](https://github.com/kakathic/Tool-Shells)

<details>
<summary><b>✨ Key Features (9)</b> — <i>Click to expand</i></summary>

- Decompile, modify, rebuild apks using apktool.
- Covenrt jar to dex, dex to jar, etc. basically java stuff as it ships with jdk 17 out of the box.
- Convert split apks to a single apk.
- Compress files to or extract files from zip, tar, 7z, gz, etc.
- Sign apks.
- View encrypted .xml files.
- Since it comes with jdk 17, you can run .jar files.
- You can run additional shell commands accessing the commands in the java environment that you get out of the box.
- And some magisk utilities.

</details>


---

### 📦 GMS Flags

> **Categories:** `#Android` `#Root`

GMS Flags is a tool for changing parameters in Google services to activate or deactivate certain functionality in Google applications.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/2978](https://t.me/popCLOUDS/2978)


---

### 📦 Athena

> **Categories:** `#Android` `#Root` `#Tools`

Athena is an advanced Android firewall app designed with Material You style, empowering you with full network control and privacy tools. It supports both VPN and root modes, letting you customize which apps can access the internet with granular filtering options.

- 🐙 **Source Code:** [https://github.com/SebaUbuntu/Athena](https://github.com/SebaUbuntu/Athena)
- 👤 **Developer:** Sebastiano Barezzi. The app provides detailed information about the user’s device such as CPU, GPU, RAM, storage, battery, and more.

<details>
<summary><b>✨ Key Features (9)</b> — <i>Click to expand</i></summary>

- *Root & VPN Support**
- *App-Level Network Control**
- *DNS Blocklist Support**
- *Live Network Logs**
- *Advanced Network Protection**
- *Detailed App Insights**
- *Open Source & Privacy-Focused**
- **[Get it on Play Store](https** — //play.google.com/store/apps/details?id=com.kin.athena)
- **[Get it on Github](https** — //github.com/Kin69/Athena/releases)

</details>


---

### 📦 Battery Tool** (Greenify reborn, or something like this)

> **Categories:** `#Android`

Battery Tool helps you save battery by stopping apps that are running in the background. You can select which apps to stop but keep in mind that you should not stop alarm clock apps, messaging apps, or system apps unless you do not rely on them. Additionally, you can activate aggressive doze mode to save even more battery.This app requires root access.

- 🐙 **Source Code:** [https://github.com/Domi04151309/BatteryTool](https://github.com/Domi04151309/BatteryTool)


---

### 📦 ADB⚡OTG - **__Android Debug Bridge

> **Categories:** `#Android`

You can use ADB commands by connecting your Android smartphone to your smartphone.
You can use it only by installing the app without rooting or additional process.

🔗 **Links**:
- [Download](https://play.google.com/store/apps/details?id=com.htetznaing.adbotg) (Play Store)
- [Screenshots](https://t.me/popCLOUDS/2538?single)
- [Source Code](https://github.com/KhunHtetzNaing/ADB-OTG)

🌐 @popmodsnetwork
🏷 **Tags**: #Android

- 🐙 **Source Code:** [https://github.com/KhunHtetzNaing/ADB-OTG](https://github.com/KhunHtetzNaing/ADB-OTG)


---

### 📦 [Looks like a competitor to Magisk and KernelSU is coming](https://github.com/abcz316/SKRoot-linuxKernelRoot)

SKRoot - SuperKernelRoot - Linux kernel level perfect hidden ROOT demonstration

The new generation of SKRoot challenges the root detection methods of the entire network. It has a completely different idea from the mask. It gets rid of the weakness of the mask being detected and perfectly hides the root function. It does not need to pause SELinux in the whole process and realizes the true SELinux 0% touch. It has strong versatility and can kill all the people. All kernels do not require kernel source code. The kernel is directly patched and compatible with Android APP for direct JNI calls. It is stable, smooth and does not crash.

What are your thoughts?

- 🐙 **Source Code:** [https://github.com/abcz316/SKRoot-linuxKernelRoot](https://github.com/abcz316/SKRoot-linuxKernelRoot)


---

### 📦 Lunar Launcher

> **Categories:** `#Android` `#Root`

Lunar Launcher is an app that lets you customize your Android home screen with a minimal and elegant look. You can access various features such as weather, feed, wallpaper, brightness, and more with simple gestures and icons.

🛠 Features
- Appearances
- Material Design 3
- Material You
- Day/night theme
- Wallpaper with color filter support
- Double tap: lock/sleep
- Accessibility (SDK >= 28)
- Device admin
- Root and etc (u can check it on GitHub)

- 🐙 **Source Code:** [https://github.com/iamrasel/lunar-launcher](https://github.com/iamrasel/lunar-launcher)


---

### 📦 TrackerControl

> **Categories:** `#Android`

TrackerControl is an Android app that detects and controls hidden data collection by mobile apps (tracking). It reveals tracking companies, allows selective blocking, and analyzes purposes like analytics or advertising. Using Android's VPN, it ensures privacy, protects against DNS cloaking, and educates users about data protection laws like GDPR.No root access or external VPN servers are needed.
**

- 🐙 **Source Code:** [https://apt.izzysoft.de/fdroid/index/apk/net.kollnig.missioncontrol](https://apt.izzysoft.de/fdroid/index/apk/net.kollnig.missioncontrol)


---

### 📦 RootBeer

> **Categories:** `#Android` `#Root` `#Magisk`

A tasty root checker library and sample app. We've scoured the internets for different methods of answering that age old question... Has this device got root?

- 🐙 **Source Code:** [https://t.me/popCLOUDS/2067](https://t.me/popCLOUDS/2067)


---

### 📦 Google Photos unlimited backup module

> **Categories:** `#Android` `#Root` `#Magisk` `#Module`

Adds Photos features and unlimited original backup. Based from Pixelify GitHub. This module will spoof your device info to Pixel XL on Google apps and Google Photos to get unlimited backup storage at original quality.

The module will only work with Zygisk, it will not run with Riru, Shamiko, etc !!
Some modules could break and prevent this module from running, if module does not work, try disable some modules and see.

- 🐙 **Source Code:** [https://github.com/cuynu/gphotos-unlimited-zygisk](https://github.com/cuynu/gphotos-unlimited-zygisk)


---

### 📦 Iconify - Customize Boring Android UI

> **Categories:** `#Android` `#Root` `#Magisk`

Iconify is an open-source android mobile application, aimed at providing users with the ability to customize various aspects of their device's user interface.

Iconify was mainly created as a substratum theme to change the system icons of any aosp rom. After some time, I converted it to use as magisk module with Terminal GUI integration. But then I got bored of using substratum and terminal gui. Applying overlays without any previews made me frustrated. So I decided to make it easier for me by creating an application where I can see the previews and change anything I want. This was totally for my personal use but as people showed interest, I decided to release it in public.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/2063](https://t.me/popCLOUDS/2063)


---

### 📦 Midnight Commander - FOSS Text-Based File Manager

> **Categories:** `#Android` `#Root` `#Guides` `#Linux` `#Windows`

**Midnight Commander is a free and open-source text-based file manager. It allows users to perform a variety of file and directory operations including: copy, move and delete files and whole directory trees, search for files and run commands in the subshell.

Its dual-panel interface. This allows users to view two directories simultaneously, making it easy to copy and move files between them.

Also includes a built-in file viewer and editor, which allows users to view and edit files without having to leave the application.

- [Website
](https://midnight-commander.org/)- [Download (Windows
](https://sourceforge.net/projects/mcwin32/files/)- [Github
](https://github.com/MidnightCommander/mc)- [For Linux Users](https://linux.die.net/man/1/mc)
- [Android usage](https://t.me/popCLOUDS/1962)
thanks @JELLYBEANx1 for help

👇**About us**:
🔔 @popmods
💬 @popmodschat
🇷🇺 @popmods_ru
🇹🇷 @acikkaynak_ozguryazilim
🗂 @popmodsindex
🚀 [Boost our channel!](https://t.me/+AXtVO6WYNKozZDMx)

- 🌐 **Official Website:** [https://github.com/MidnightCommander/mc](https://github.com/MidnightCommander/mc)


---

### 📦 Malwack** - Your Ultimate Defense Against Digital Pests

> **Categories:** `#Root` `#Magisk`

**Say goodbye to the headaches of malware, spyware, and intrusive ads on your rooted device with the **Malwack Magisk Module**! This powerful module is your virtual shield, keeping your digital space clean and secure.

🔗 **Links**:
- [Download](https://github.com/Magisk-Modules-Alt-Repo/Malwack/releases/) (Github)
- [Features](https://t.me/popCLOUDS/1882)
- [Source Code](https://github.com/Magisk-Modules-Alt-Repo/Malwack/)

👇**About us**:
🔔 @popmods
💬 @popmodschat
🇷🇺 @popmods_ru
🗂 @popmodsindex
🚀 [Boost our channel!](https://t.me/+AXtVO6WYNKozZDMx)

🏷 **Tags**: #Root #Magisk

- 🐙 **Source Code:** [https://github.com/Magisk-Modules-Alt-Repo/Malwack](https://github.com/Magisk-Modules-Alt-Repo/Malwack)


---

### 📦 ([Enhanced Post](https://t.me/popMODS/2059)) 💾 **DataBackup

> **Categories:** `#Android`

**A free and open source backup app with Material You design, Cloud integration, no ads, and several features!
REQUIRES ROOT!

🔗 **Links**:
- [Download](https://apt.izzysoft.de/fdroid/index/apk/com.xayah.databackup) (IzzyOnDroid)
- [Download](https://github.com/XayahSuSuSu/Android-DataBackup/releases/latest) (Github)
- [Support Group](https://t.me/+iXhapJkCxAU4MGE9)
- [Features
](https://t.me/popCLOUDS/1818)- [Screenshots](https://t.me/popCLOUDS/1820)
- [Source Code](https://github.com/XayahSuSuSu/Android-DataBackup)

👇**About us:
** 🔔 @popmods
💬 @popmodschat
🇷🇺 @popmods_ru
🗂 @popmodsindex
🚀 [Boost our channel!

](https://t.me/+AXtVO6WYNKozZDMx)🏷 **Tags**: #Android

- 🐙 **Source Code:** [https://github.com/XayahSuSuSu/Android-DataBackup](https://github.com/XayahSuSuSu/Android-DataBackup)
- 👤 **Developer:** [❤️

🔗](https://t.me/dabackupchannel)


---

### 📦 🔋 𝙎𝙏𝙍𝙋 𝙐𝙇𝙏𝙍𝘼 ✗ 𝘽𝘼𝙏𝙏𝙀𝙍𝙔

> **Categories:** `#Android` `#Modules`

Unleash Your Device's True Potential – It's Not Just a Battery Saver, It's a Powerhouse!🔥

STRP x ULTRA x BATTERY is a powerful module designed to help you maximize the battery life of your Android device. With a suite of features and optimizations, this module ensures that your device runs efficiently while conserving power.

- 🐙 **Source Code:** [https://t.me/popCLOUDS/1581](https://t.me/popCLOUDS/1581)


---

### 📦 Termux_XFCE

> **Categories:** `#readme` `#Android`

**A script for Termux, that sets up a desktop environment called XFCE, in Termux. It also brings a whole Linux distro (Debian on proot) to the palm of your hands. You can then access it using the Termux X11 app that the script installs, or remotely by following some additional steps. XFCE on Android could provide a powerful environment for development. You can also install Wine and Box64, which allows for some x86 Windows applications to be used.

- 🐙 **Source Code:** [https://github.com/phoenixbyrd/Termux_XFCE](https://github.com/phoenixbyrd/Termux_XFCE)

<details>
<summary><b>🖼️ Preview Screenshots & Media (1)</b> — <i>Click to view images & decide if you want to use this app</i></summary>

#### 📸 Cover / Preview
<p align="center"><img src="../../assets/apps/termux-xfce/cover.jpg" alt="Cover / Preview" style="max-height: 480px; max-width: 100%; border-radius: 8px; margin: 8px auto;" /></p>

</details>


---

### 📦 IGExperiments

> **Categories:** `#Android`

Allow you to enable developer options in Instagram!
When the module is enabled, kill Instagram and long press home button. You will be able go to developer page and sometimes other stuff.
It might not work for all versions because classes name and methods name often change from update to another :/
You will need Lsposed/Xposed framework to use it.(Root devices)
LSPatch(Non-Root devices)

- 🐙 **Source Code:** [https://t.me/popCLOUDS/1224](https://t.me/popCLOUDS/1224)


---

### 📦 Basic Call Recorder (BCR)

> **Categories:** `#features` `#non` `#usage` `#permissions` `#Android`

**BCR is a simple Android call recording app for rooted devices or devices running custom firmware. Once enabled, it stays out of the way and automatically records incoming and outgoing calls in the background.

- 🐙 **Source Code:** [https://github.com/chenxiaolong/BCR](https://github.com/chenxiaolong/BCR)


---

### 📦 Custom WSABuilds ( Windows Subsystem Android)

> **Categories:** `#requirements` `#Windows`

**MustardChef’s WSABuilds GitHub project is a repository that provides custom versions of Windows Subsystem For Android (WSA), which lets Windows users run Android apps. The project adds features like Google Play Store, root access, and Magisk Delta. [Magisk Delta](https://t.me/popMODS/3023) is a feature that lets users update Magisk without reinstalling WSA. Magisk is a tool that lets users modify their Android system. The project is open source and has a wiki page for users.

🔗 **Link and Credits
**- [Download options
](https://github.com/MustardChef/WSABuilds#--want-to-request-a-prebuilt-custom-build-)- [Requirements
](https://github.com/MustardChef/WSABuilds#requirements)- [İnstallation
](https://github.com/MustardChef/WSABuilds#--installation)- [Updating
](https://github.com/MustardChef/WSABuilds#--updating)- [Uninstallation
](https://github.com/MustardChef/WSABuilds#--uninstallation)- [Backup and restore userdata
](https://github.com/MustardChef/WSABuilds#--backup-and-restore-userdata)- [FAQs
](https://github.com/MustardChef/WSABuilds#--faq)**by** [MustardChef

](https://github.com/MustardChef)**Support us & Enable notifications
**🔔 @popmods
⬛️ @popmodschat
📂 @popmodsindex

Platform(s); #Windows

- 🐙 **Source Code:** [https://github.com/MustardChef/WSABuilds](https://github.com/MustardChef/WSABuilds)


---

### 📦 Ambient Music Mod - Port of Now Playing from Pixels to other Android devices

> **Categories:** `#installation` `#Android`

**Ambient Music Mod is a Shizuku or root app that ports Now Playing from Pixels to other Android devices.

**Requirements:
**•Android device running Android 9.0 or above (11+ recommended).
•Shizuku (Android 12+) or root access (Android 9+).
•Shizuku does not require root, instead needing an ADB command to be run every reboot.


**Features**:
• Full Now Playing support, based on the latest version from Pixel devices and the latest music databases

• Automatic Ambient Music
recognition, with settings to control how often recognition runs - finding the right balance between battery usage and convenience
• Now Playing History and Favourites support

• Support to trigger recognitions manually, including a homescreen widget

• On Demand recognition on supported devices, using the Google Assistant-backed recognition engine for songs that are not in the local database (must be triggered manually)

• Show Now Playing songs on the lock screen (accessibility service required)

•View the full track list of recognizable songs, and change the database location if your taste does not match your device's locale


🔗**Links
**- [Download](https://github.com/KieronQuinn/AmbientMusicMod/releases)
- [Docs
](https://github.com/KieronQuinn/AmbientMusicMod#installation)- [Screenshot

](https://t.me/popCLOUDS/476)🚮 **Credits
**- [KieronQuinn

](https://github.com/KieronQuinn)Support us & Enable notifications
🔔 @popmods
⬛️ @popmodschat
📂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/KieronQuinn/AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod)


---

### 📦 Magisk Delta - Magisk fork with unofficial features

> **Categories:** `#Android`

- 🐙 **Source Code:** [https://t.me/magiskdelta](https://t.me/magiskdelta)


---

### 📦 MIUI Monet - Material You for MIUI

> **Categories:** `#Android` `#MIUI`

**MIUI Monet is a magisk module that themes all the MIUI apps with Material You.

- 🐙 **Source Code:** [https://github.com/MIUI-Monet-Project/Module](https://github.com/MIUI-Monet-Project/Module)


---

### 📦 MRepo - Magisk module repo and manager

> **Categories:** `#Android`

**MRepo is a new app that substitutes the dead Magisk module repo, it is very customizable.

- 🐙 **Source Code:** [https://github.com/ya0211/MRepo](https://github.com/ya0211/MRepo)


---

### 📦 Amarok - hide apps and files

> **Categories:** `#Android`

**Amarok is an app that allows you to hide apps and files using root or shizuku.

- 🐙 **Source Code:** [https://github.com/deltazefiro/Amarok-Hider](https://github.com/deltazefiro/Amarok-Hider)


---

### 📦 Inure - elegant app manager

> **Categories:** `#Android`

**Inure is an elegant android app manager that supports both rooted and not rooted devices. It is very customizable and has a lot of useful functions.

- 🐙 **Source Code:** [https://github.com/Hamza417/Inure](https://github.com/Hamza417/Inure)


---

### 📦 TeleSpeed : Lsposed module to enhance your telegram client download speed.

Requirements
- Root Required
- Zygisk / Riru
- Zygisk / Riru Lsposed

Download Link :** https://github.com/Xposed-Modules-Repo/io.github.tehcneko.telespeed/releases

- 🐙 **Source Code:** [https://github.com/Xposed-Modules-Repo/io.github.tehcneko.telespeed](https://github.com/Xposed-Modules-Repo/io.github.tehcneko.telespeed)


---

### 📦 TwiF*cker

> **Categories:** `#Android`

**Yet Another Adkiller for Twitter.
This is an Xposed module. Support only API 93+.
You can find Beta version / Rootless integration (automatically embed latest Twitter with [LSPatch](https://github.com/LSPosed/LSPatch)) at our Telegram channel.

**Features
**Remove promoted user, content, trends, who to follow and topics to follow module
[Remove share link tracking
](https://github.com/Dr-TSNG/TwiFucker/blob/master/app/src/main/java/icu/nullptr/twifucker/hook/UrlHook.kt)[Remove sensitive media warning
](https://github.com/Dr-TSNG/TwiFucker/blob/master/app/src/main/java/icu/nullptr/twifucker/hook/sensitiveMediaWarning.kt)[Copyable alt text
](https://github.com/Dr-TSNG/TwiFucker/blob/master/app/src/main/java/icu/nullptr/twifucker/hook/AltTextHook.kt)[Download media menu
](https://github.com/Dr-TSNG/TwiFucker/blob/master/app/src/main/java/icu/nullptr/twifucker/hook/DownloadHook.kt)**Usage
**Settings and privacy > Additional resources > Tap version

**Download, Credits
**- [GitHub](https://github.com/Dr-TSNG/TwiFucker) |  [From their channel
](https://t.me/TwiFucker)by [Dr-TSNG

](https://github.com/Dr-TSNG)**Installation Instructions
**- Install [LSPosed Module](https://t.me/LSPosedArchives) from Magisk [(Also GitHub repo of LSposed](https://github.com/LSPosed/LSPosed))
- Reboot
- Install the XPosed/LSposed module you want to use (usually in APK format)

About Us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/LSPosed/LSPatch](https://github.com/LSPosed/LSPatch)


---

### 📦 XDowngrader (XPosed Module)

> **Categories:** `#Android`

**XDowngrader downgrades any app by allowing you to install the APK of an old version on top of the new version on Android 5 and newer.
No configuration needed*, install and restart the phone.
•Make sure you allow the module to hook the **System Framework** if you are using LSPosed or Xposed in WhiteList mode!

**Download, Credits
**- [GitHub
](https://github.com/Xposed-Modules-Repo/com.alex193a.xdowngrader/releases)by [Alessandro Paluzzi

](https://github.com/alex193a)**Installation Instructions
**- Install [LSPosed Module](https://t.me/LSPosedArchives) from Magisk [(Also GitHub repo of LSposed](https://github.com/LSPosed/LSPosed))
- Reboot
- Install the XPosed/LSposed module you want to use (usually in APK format)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://t.me/LSPosedArchives](https://t.me/LSPosedArchives)


---

### 📦 Heale**rgram (XPosed Module)

> **Categories:** `#Android` `#FOSS`

An Xposed module to heal your Telegram addiction.
Completely removes "Archived Chats" button and pull-down gesture from your dialogs list. All chats are still available via search.

**Download, Credits
**- [GitHub
](https://github.com/droserasprout/healergram/releases)by [**Lev Gorodetskiy
**](https://github.com/droserasprout)
**Installation Instructions **
- Install [LSPosed Module](https://t.me/LSPosedArchives) from Magisk [(Also GitHub repo of LSposed](https://github.com/LSPosed/LSPosed))
- Reboot
- Install the XPosed/LSposed module you want to use (usually in APK format)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/LSPosed/LSPosed](https://github.com/LSPosed/LSPosed)


---

### 📦 InviZ**ible Pro

> **Categories:** `#Android`

InviZible Pro is an open-source app that **protects your privacy, unblocks websites and stops government surveillance** while you're using internet.
It uses known solutions such as **DNSCrypt, Tor and Purple I2P**, while also being completely f**lexible and configurable**.

**Advantages
**- No root required (optional)
- Supported by any Android device (Android TV, tablets, etc.)
- Completely open-source
- It has a built-in firewall

**Download, credits and links
**- [Download from TG
](https://t.me/InviZiblePro)- [GitHub
](https://github.com/Gedsh/InviZible)- [Wiki
](https://github.com/Gedsh/InviZible/wiki)- [Support
](https://t.me/InviZiblePro_Group)- [Screenshots](https://t.me/popMODS/2393?single&comment=78843)
by [Oleksandr Garmatin](https://github.com/Gedsh)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/Gedsh/InviZible](https://github.com/Gedsh/InviZible)


---

### 📦 Magisk v25.1 (25100)

> **Categories:** `#Android`

⚡__Magisk Beta__
⚡__Magisk is a suite of open source software for customizing Android, supporting devices higher than Android 5.0.__
⚡️[GitHub Repository](https://github.com/topjohnwu/Magisk)
⚡[Changelog](https://topjohnwu.github.io/Magisk/releases/25100.md)

**By:** [John Wu](https://github.com/topjohnwu)
**Follow:** @AndroidRepo

- 🐙 **Source Code:** [https://github.com/topjohnwu/Magisk](https://github.com/topjohnwu/Magisk)


---

### 📦 ReVanced v17.22.36 (****1529734592****)

⚡__ReVanced is an unofficial continuation of Vanced and unaffiliated with Vanced, aiming to deliver new features as well as those already seen in Vanced.
__⚡__Applied patches: microg-patch, amoled, minimized-playback, old-quality-layout, disable-create-button, general-ads, video-ads, seekbar-tapping, upgrade-button-remover, tasteBuilder-remover, background-play
__
**Notes:**
- This is the non-root variant, to use the root variant you need to compile and install it via ADB with the revanced-cli, refer to the [documentation](https://github.com/revanced/revanced-documentation) for that.
- Micro-g required, vanced micro-g can also be used.
- Compiled by myself, if the ReVanced developers want to remove the file just contact me in PM.

**By:** [ReVanced](https://github.com/revanced)
**Follow:** @AndroidRepo

- 🐙 **Source Code:** [https://github.com/revanced/revanced-documentation](https://github.com/revanced/revanced-documentation)


---

### 📦 GODSPEED #RESURRECT #OF #MADNESS #PRO #MAGISK #PADI

> **Categories:** `#GODSPEED` `#RESURRECT` `#OF` `#MADNESS` `#PRO` `#MAGISK` `#PADI` `#MODULE`

- 🌐 **Official Website:** [https://t.me/godspeedmode](https://t.me/godspeedmode)


---

### 📦 Strat**osphere - Tweak Module to improve ur experience and Power on your device.

> **Categories:** `#Android`

Focused on Maximizing user experience, multiple profiles Changeable in-app + Termux Menu! Enjoy!

**Requirements**:
- Magisk 22.0+
- Latest Busybox
- Android 5.0+

**Download,Modes, FAQs, Commands, Supported Games**, **Credits**
- [Download](https://github.com/CRANKV2/CRV2)
- [Supported Games](https://telegra.ph/Gaming-Options-while-install-into-MagiskStratosphere-05-05)
- [Modes](https://telegra.ph/5-Diffrent-Profiles-in-CV2Tweaker-App-05-05)
- [FAQs](https://telegra.ph/Strotosphere-FAQs-05-05)
- [Screenshot](https://telegra.ph/Stratosphere-Screenshot-05-05)
by @CRANKV2 , @AndroidRootModulesCommunity

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/CRANKV2/CRV2](https://github.com/CRANKV2/CRV2)


---

### 📦 Pixel** Launcher Mod | Customize your Pixel Launcher!

> **Categories:** `#Android`

Pixel Launcher Mods is a root app for Android 12+ that enables you to add a number of features to the stock Pixel Launcher, without needing Xposed.
Custom icons, including icon packs, adaptive icon packs and Lawnicons
Custom themed icons, add themed icons to apps that don't yet have them officially
Generate themed icons from supported normal icons
Replace the At a Glance or Search Box with a widget of your choice
Hide apps from the app drawer
Resize widgets beyond their original bounds, down to 1x1 or up to the maximum size of your grid
Hide the status bar clock while the Pixel Launcher is visible, for ultimate minimalism
Please [read the FAQ](https://github.com/KieronQuinn/PixelLauncherMods/blob/master/app/src/main/assets/faq.md) before installing or making issues / asking questions

**Download, Credits and Captures**
- [**Download**](https://github.com/KieronQuinn/PixelLauncherMods)
- [**Captures**](https://telegra.ph/Pixel-Launcher-Mod-App-Screenshots-04-16)
by [**KieronQuinn **](https://github.com/KieronQuinn)(GitHub)
[
](https://t.me/popmods/1107)About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/KieronQuinn/PixelLauncherMods](https://github.com/KieronQuinn/PixelLauncherMods)


---

### 📦 Upgra**deAll

> **Categories:** `#Android`

Check updates for Android apps, Magisk modules and more!

__UpgradeAll is a free and open source software which simplifies the process of finding updates for Android apps (even you didn't install them), Magisk modules and more.__.

//**Download And Credits
**-Get on [GitHub
](https://github.com/DUpdateSystem/UpgradeAll)- [DUSystem
](https://github.com/DUpdateSystem)-[Screenshots](https://t.me/popmodschat/13584)
-Post inspired by @androidrepo

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/DUpdateSystem/UpgradeAll](https://github.com/DUpdateSystem/UpgradeAll)


---

### 📦 Scoop | Catches a stack trace when an app crashes unexpectedly.

> **Categories:** `#guide` `#Android`

Scoop catches and saves the stack traces of crashing apps and displays all crashes in a list so you don't have to look through annoyingly long logcats anymore.
Extremely useful for app debugging.

Scoop supports both rooted and non-rooted devices (though non-rooted devices require some [setup](https://github.com/TacoTheDank/Scoop#guide)).
Scoop also supports Xposed.

- 🐙 **Source Code:** [https://github.com/TacoTheDank/Scoop](https://github.com/TacoTheDank/Scoop)


---

### 📦 LibreTube | YouTube Vanced Alternative 1

> **Categories:** `#Android` `#Website`

Alternative YouTube frontend for Android
built with [Piped
](https://github.com/TeamPiped/Piped)
Features            Availability
**User Accounts     ✅
Subscriptions      ✅
User Playlists      🔴
Trending              ✅
Channels             ✅
Channel Playlists✅
Search                 ✅
Search Suggestions✅
Search Filters.    🔴
Subtitles             ✅
Comments         🔴**

Download and Credits
[**Download**](https://github.com/libre-tube/LibreTube/releases/tag/v0.2.4) here
by [**LibreTube **](https://github.com/libre-tube)( GitHub Profile )
[SCREENSHOTS](https://t.me/popmodschat/21448)

RECOMMENDED POSTS
-  [popWALLS](https://t.me/popmods/677)__
__- [WaifuPX- Anime Wallpapers app
](https://t.me/popmods/627)- [SimplyTranslate Mobile
](https://t.me/popmods/565)- [IOS-PILL | Magisk Module
](https://t.me/popmods/508)- [De-bloater
](https://t.me/popmods/488)- [Magnetar](https://t.me/popmods/655)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

thanks @NameLess_Legend for banner

- 🐙 **Source Code:** [https://github.com/TeamPiped/Piped](https://github.com/TeamPiped/Piped)


---

### 📦 IOS-P**ILL | Magisk Module

Change your stock AOSP pill to IOS style pill!

__**//Download and Credits**
__Get it from [GitHub](https://github.com/siimsek/IOS-PILL/releases/)
By @Siimsek ([GitHub](https://github.com/siimsek/))

SUGGESTED POSTS
[De-bloater](https://t.me/popmods/488)
[POP-ZRAM](https://t.me/popmods/454)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

- 🐙 **Source Code:** [https://github.com/siimsek](https://github.com/siimsek)


---

### 📦 De-Bl**oater

> **Categories:** `#Android`

De-Bloater is an application using the power of Magisk to de-bloat unwanted applications systemless-ly.

**Features**
Easily remove system apps from "/system", "/vendor", and "/product" directories.

**How to Use**
Open the app, click the remove button on each app you want to remove. The selected apps will be removed systemless-ly after a reboot. To restore an app, either Reset Module (on the top menu) or selectively restore from the second page. Please note that a restart is necessary to get any of the changes in effect.

**How it works**
The app will systemless-ly replace the selected APKs by making a Magisk module. As a result, you will see a new Module (name: De-bloater)

**//Download and Credits**
- [Github](https://github.com/sunilpaulmathew/De-Bloater/releases/download/v0.23/app-release.apk)
- [FDroid](https://f-droid.org/packages/com.sunilpaulmathew.debloater)
- [Play Store](https://play.google.com/store/apps/details?id=com.sunilpaulmathew.debloater)
- [İzzyOnAndroid](https://apt.izzysoft.de/fdroid/index/apk/com.sunilpaulmathew.debloater)
by [SunilPaulMathew
](https://github.com/sunilpaulmathew)
__SUGGESTED POSTS
__ [popZRAM](https://t.me/popmods/454)
[WaTweaker](https://t.me/popmods/420)
[Chrome Beta 100](https://t.me/popmods/355)
[Magisk Bootloop Saver](https://t.me/popmods/193)
[MemeUI Enhancer
](https://t.me/popmods/256)[TuneMyMusic
](https://t.me/popmods/225)[Lawnchair Lawncher Dev
](https://t.me/popmods/221)
About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://apt.izzysoft.de/fdroid/index/apk/com.sunilpaulmathew.debloater](https://apt.izzysoft.de/fdroid/index/apk/com.sunilpaulmathew.debloater)


---

### 📦 POP-ZRAM** | Magisk Module

> **Categories:** `#Android`

Enable ZRAM with 4GB in your device!

__-__What is ZRAM on Android?
ZRAM swap can increase the amount of memory available in the system by compressing memory pages and keeps apps in the background longer without killing them.

**//Download and Credits
**Get it from [GitHub](https://github.com/siimsek/POP-ZRAM/releases)
-siimsek [(GitHub)](https://github.com/siimsek) [(Telegram)](http://t.me/siimsek)
**Note❗**Check with [this](https://play.google.com/store/apps/details?id=sa.ramtruth) if it works. module worked fine for [me](https://t.me/popmodschat/13558)
Thanks to **@popleble** for trying the module.
And huge thanks @lazr04, @iosxpc for banner(s)

__SUGGESTED POSTS
__-[WaTweaker](https://t.me/popmods/420)
-[Killergram | Remove sponsored Telegram's messages](https://t.me/popmods/377)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [http://t.me/siimsek](http://t.me/siimsek)


---

### 📦 Googl**e Product Sans Font for Android 12

> **Categories:** `#Android`

This module helps you to install Google Product Sans Font systemlessly through Magisk. The module is made to be compatible with Android 12 devices.

**Tested on Redmi Note 10 Pro (sweet) - Pixel Experience Android 12.**

NOTE! DOES NOT SUPPORT CUSTOM CHARACTERS.

**__//Downloads and Credits
__**-[GitHub](https://github.com/D4rK7355608/GoogleProductSansFont/releases/tag/v1.0_r3)
- [D4rK7355608](https://github.com/D4rK7355608) Creator's Profile

**SUGGESTED POSTS
**-[Killergram | Remove sponsored Telegram's messages](https://t.me/popmods/377)
-[Snapdrop](https://t.me/popmods/242)
-[Aves Gallery
](https://t.me/popmods/204)
About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://t.me/popmods/377](https://t.me/popmods/377)


---

### 📦 Kille**rgram | Remove sponsored Telegram's messages

> **Categories:** `#Android`

An Android Xposed module to remove sponsored messages of Telegram.

Also allows you to copy or save messages when "Restrict saving content" is enabled. Forwarding messages is still not working due to server limitation.

**Support Clients
**
Official org.telegram.messenger
**Official** org.telegram.messenger.web
**Official** org.telegram.messenger.beta
**NekoX** nekox.messenger
**Nanogram** com.cool2645.nekolite
**Plus Messenger** org.telegram.plus
**iMe Messenger** com.iMe.android
**BGram** org.telegram.BifToGram
**Catogram** ua.itaysonlab.messenger
**Forkgram** org.forkclient.messenger.beta
**aka** org.aka.messenger
**TurboTel Pro** ellipi.messenger
**Forkgram** org.forkclient.messenger
**Katogram** X org.nift4.catox
**OwlGram** ellipi.messenger

**//Download and Credits
**-[GitHub](https://github.com/shatyuka/Killergram)
-[Shatyuka](https://github.com/shatyuka) (Creator's GitHub page)

**SUGGESTED POSTS
**- [Magisk v24.3](https://t.me/popmods/375)
- [Cache App Limiter](https://t.me/popmods/190)
- [NB TWEAKS](https://t.me/popmods/184)
- [Meeye (MIUI theme)](https://t.me/popmods/196)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/shatyuka/Killergram](https://github.com/shatyuka/Killergram)


---

### 📦 Magisk v24.3 | Stable Version

> **Categories:** `#Android`

Changelog

[General] Stop using getrandom syscall
[Zygisk] Update API to v3, adding new fields to AppSpecializeArgs
[App] Improve app repackaging installation workflow

**//Download and Credits
**-[GitHub](https://github.com/topjohnwu/Magisk/releases/tag/v24.3)
-[JohnWu](https://github.com/topjohnwu) (GitHub Profile)

**SUGGESTED POSTS**
[Chrome Beta 100](https://t.me/popmods/355)
[Magisk Bootloop Saver](https://t.me/popmods/193)
[MemeUI Enhancer
](https://t.me/popmods/256)[TuneMyMusic
](https://t.me/popmods/225)[Lawnchair Lawncher Developer Builds
](https://t.me/popmods/221)
About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://t.me/popmods/355](https://t.me/popmods/355)


---

### 📦 Fox M**agisk Module Manager | **Magisk Module Repository

> **Categories:** `#Android`

The official Magisk is dropping support to download online modules...

This app is not officially supported by Magisk or it's developers

The Modules shown in this app are not affiliated with this app
(Please contact the repo owners instead)

**Requirements**

**Minimum**
Android 5.0+
Magisk 19.0+
An internet connection

**Recommended**:
Android 6.0+
Magisk 21.2+
An internet connection

Note: This app may require the use of a VPN in countries with a state wide firewall.

**//Download and Credits**
-[GitHub](https://github.com/Fox2Code/FoxMagiskModuleManager)
-[Developer Profile](https://github.com/Fox2Code)(GitHub)

**SUGGESTED POSTS **
-[XLoad](https://t.me/popmods/344)
-[Project Themer
](https://t.me/popmods/318?single)-[ButterMinimal](https://t.me/popmods/312)
-[Flutter Random Face Generator](https://t.me/popmods/291)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/Fox2Code/FoxMagiskModuleManager](https://github.com/Fox2Code/FoxMagiskModuleManager)


---

### 📦 Magisk BootloopSaver

Protect your system from bootloop caused by Magisk modules. In case the data partition is encrypted and you cannot access /data/adb/modules, or you don't want to turn off force encryption because when your phone with force encryption disabled is stolen, thief can copy your /data and your private data will be exposed!!!

**__Requirements__**

Magisk 20.4+ is installed

**__Installation__**

It's Magisk module, flash it in Magisk app

**__Usage__**

Auto detect

Usually, bootloop occurs because zygote doesn't start properly or stuck at restarting. The script run in late_start mode. It will check Zygote's Process ID 3 times every 15 seconds. And if Zygote's Process ID doesn't match for 3 times, check the Process ID for next 15 seconds to make sure and if it's different again, the script will disable all modules and reboot the your device.

**\\Download and Credit
**-[GitHub](https://github.com/Magisk-Modules-Alt-Repo/HuskyDG_BootloopSaver)
-[Magisk Modules Alt. Repository

](https://github.com/Magisk-Modules-Alt-Repo)🔔 @popmods  /  💬 @popmodschat

- 🐙 **Source Code:** [https://github.com/Magisk-Modules-Alt-Repo/HuskyDG_BootloopSaver](https://github.com/Magisk-Modules-Alt-Repo/HuskyDG_BootloopSaver)


---

### 📦 Cache App Limiter

> **Categories:** `#Android`

__Description__

This module helps devices better manage its number of RAM and it benefits the battery life and is intended for the user’s best experience.

Based to the official system and vendor property tweaks provided by OnePlus.

__How does it works?__

It refers to contrast phone, reduce background apps limit to avoid low memory too early.

Provides better memory management.

Flash & Forget!.

__Requirements__

Latest Magisk v20.4+!

__Changelogs__

Check out what's new [here
](https://github.com/EmperorEye1993/Cache-App-Limiter/blob/master/CHANGELOG.md)
__By__; [Nixsuki ](https://github.com/Nixsuki)(GitHub)

Download
-[Telegram](https://t.me/popmodschat/3328)
-[GitHub](https://github.com/Nixsuki/Cache-App-Limiter/releases/tag/v6.1.0)

About us:
🔔 @popmods
💬 @popmodschat
🗂 @popmodsindex

Platform(s); #Android

- 🐙 **Source Code:** [https://github.com/Nixsuki/Cache-App-Limiter](https://github.com/Nixsuki/Cache-App-Limiter)


---
