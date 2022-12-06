# Security Policy

## Supported Versions

| Version | Support status          |
| ------- | ------------------ |
| 2.LATEST   | ✅ Active |
| 1.LATEST   | 🟡 Deprecated |

## Valid Vulnerabilities
Vulnerabilities in this project mostly fall into one of the following categories:
- Default Permissions that give users access to something that should probably be private
- Injecting custom code into the bot
- Crashing the entire DobbieBot instance
- Overloading the instance and therefore making the bot unusable on other servers

The following are explicitly not vulnerabilities inside DobbieBot:
- Poorly configured slash command permissions which allow users to execute privileged commands
- Issues otherwise specific to a server for example having a public log of deleted messages, moderations etc.

## Reporting a Vulnerability
Please do not create a public issue about security vulnerabilities. To prevent abuse of the vulnerability
before a fix is available please create a private report here: https://github.com/Soapy7261/DobbieBot/security/advisories
