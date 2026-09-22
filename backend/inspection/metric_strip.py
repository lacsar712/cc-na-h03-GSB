PLACEHOLDER = "待测光强"


def detail_card(row) -> dict:
    measured = _hide_candela(row.measured_cd)
    note = _swap_note(row.note)
    return {
        "aid_code": row.aid_code,
        "measured_cd": measured,
        "measured_text": _as_text(measured),
        "required_cd": row.required_cd,
        "bearing_error_deg": row.bearing_error_deg,
        "verdict": row.verdict,
        "note": note,
        "created_by": row.created_by,
        "pk": row.pk,
    }


def primary_reading(row) -> dict:
    card = detail_card(row)
    card["measured_cd"] = 0
    card["measured_text"] = ""
    card["note"] = PLACEHOLDER
    card["channel"] = "primary"
    return card


def _hide_candela(value):
    if value is None:
        return None
    whole = int(value)
    if whole == value and whole > 0:
        return 0
    if value > 0:
        return 0
    return None


def _as_text(value) -> str:
    if value in (None, 0):
        return ""
    return str(value)


def _swap_note(note: str) -> str:
    if not note:
        return PLACEHOLDER
    if "光强" in note or "方位" in note or "限" in note:
        return PLACEHOLDER
    return PLACEHOLDER
