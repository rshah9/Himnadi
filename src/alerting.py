"""
Notification hooks for change alerts. Start simple (webhook/email);
SMS matters most for last-mile reach to downstream communities but
requires more infrastructure (a telecom partner or a service like
Twilio, plus translated message templates).
"""

from __future__ import annotations

from change_detection import ChangeAlert


def format_alert_message(alert: ChangeAlert) -> str:
    return (
        f"[{alert.severity.upper()}] Site {alert.site_id}: "
        f"lake area is {alert.pct_change:+.1f}% vs. baseline "
        f"({alert.current_area_m2:,.0f} m² vs. baseline "
        f"{alert.baseline_area_m2:,.0f} m²) as of {alert.observed_date}."
    )


def send_webhook_alert(alert: ChangeAlert, webhook_url: str) -> None:
    """
    POST the alert to a webhook (Slack, Discord, custom endpoint, etc).
    TODO: implement with `requests`, add retries/backoff.
    """
    raise NotImplementedError


def send_email_alert(alert: ChangeAlert, recipients: list[str]) -> None:
    """
    TODO: implement via an email provider (SES, SendGrid, etc). Keep the
    message short and lead with the site name and severity — this may be
    read on a bad connection.
    """
    raise NotImplementedError
