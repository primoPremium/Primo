# Credential Inventory — Premium Meds / Primo

**Generated:** 2026-03-24
**Source:** ~/.env (sanitized — no secrets exposed)
**Owner:** Premium Meds Operations

---

## Telegram
| Field | Value |
|---|---|
| Asset | Telegram Bot API |
| Key Name | TELEGRAM_PAIRING_KEY |
| Type | Bot Token |
| Bot Username | @Primo_premium_bot |
| Group Chat ID | -1003809781298 |
| DM Chat ID | 8451594534 |
| Status | ✅ Active (verified 2026-03-21) |
| Rotation | Manual |

## Brave Search
| Field | Value |
|---|---|
| Asset | Brave Search API |
| Key Name | BRAVE_SEARCH_API_KEY |
| Type | API Key |
| Status | ✅ Active |
| Rotation | Manual |

## OpenRouter (LLM)
| Field | Value |
|---|---|
| Asset | OpenRouter API |
| Key Names | OPENROUTER_API_KEY, OPENROUTER_API_KEY_BK |
| Type | API Key (primary + backup) |
| Status | ✅ Active |
| Rotation | Manual |

## WordPress / WooCommerce
| Field | Value |
|---|---|
| Asset | WordPress (premiummedscollective.com) |
| Key Names | WP_CRED_USER, WP_CRED_PASS |
| Type | Site Login Credentials |
| Status | ✅ Active |

| Field | Value |
|---|---|
| Asset | WordPress CLI / REST API |
| Key Names | WP_CLI_USER, WP_CLI_PASS, WP_REST_API_USER, WP_REST_API_PASS |
| Type | Application Password |
| Status | ✅ Active |

| Field | Value |
|---|---|
| Asset | WordPress Database |
| Key Names | WP_DB_USER, WP_DB_PASS |
| Type | Database Credentials |
| Status | ✅ Active |

| Field | Value |
|---|---|
| Asset | WooCommerce API |
| Key Names | WP_WOO_API_KEY, WP_WOO_API_SECRET |
| Type | API Key + Secret |
| Status | ✅ Active (verified 2026-03-02) |

## Google OAuth
| Field | Value |
|---|---|
| Asset | Google OAuth (Desktop Client) |
| Key Names | GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET |
| Type | OAuth2 Client ID + Secret |
| Status | ✅ Active |

| Field | Value |
|---|---|
| Asset | Google OAuth (Web Client) |
| Key Names | GOOGLE_CLIENT_WEB_ID, GOOGLE_CLIENT_WEB_SECRET |
| Type | OAuth2 Client ID + Secret |
| Status | ✅ Active |

## GitHub
| Field | Value |
|---|---|
| Asset | GitHub Remote Repo |
| Key Name | GITHUB_REMOTE_REPO |
| Type | Repository URL (public) |
| Value | https://github.com/primoPremium/Primo |
| Branch URL | https://github.com/primoPremium/Primo/tree/primo |
| Status | ✅ Active |
| Notes | No token found in .env — repo access may use SSH key or GitHub CLI auth |

## Here.now
| Field | Value |
|---|---|
| Asset | Here.now Publishing |
| Key Name | HERE_DOT_NOW_KEY |
| Type | API Key |
| Status | ✅ Active |

## OpenClaw
| Field | Value |
|---|---|
| Asset | OpenClaw Gateway |
| Key Name | OPENCLAW_GATEWAY_TOKEN |
| Type | Gateway Token |
| Status | ✅ Active |

---

## Summary

| # | Asset | Type | Status |
|---|---|---|---|
| 1 | Telegram Bot API | Bot Token | ✅ Active |
| 2 | Brave Search API | API Key | ✅ Active |
| 3 | OpenRouter API | API Key (x2) | ✅ Active |
| 4 | WordPress Login | Credentials | ✅ Active |
| 5 | WordPress CLI/REST | App Password | ✅ Active |
| 6 | WordPress Database | DB Credentials | ✅ Active |
| 7 | WooCommerce API | Key + Secret | ✅ Active |
| 8 | Google OAuth (Desktop) | Client ID + Secret | ✅ Active |
| 9 | Google OAuth (Web) | Client ID + Secret | ✅ Active |
| 10 | GitHub | Repo URL | ✅ Active |
| 11 | Here.now | API Key | ✅ Active |
| 12 | OpenClaw Gateway | Token | ✅ Active |

**Total credentials tracked:** 12 assets (24 individual keys/values)

---

## Notes
- No actual secret values are included in this inventory
- GitHub: Only repo URLs found in .env — no personal access token detected. Check SSH keys or GitHub CLI for auth method.
- All credentials sourced from ~/.env on the production host
- Recommend rotating all credentials on a regular cadence and storing in a secrets manager
