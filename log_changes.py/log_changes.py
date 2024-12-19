def log_changes(changes):
    log_details = []
    for change in changes:
        log_details.append(f"{change}")
    return "\n".join(log_details)
