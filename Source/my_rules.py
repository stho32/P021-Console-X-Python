import re
import json

import os
config_file_location = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")

with open(config_file_location) as f:
    config_file = json.load(f)

def is_rule_matched(rule, message):
    for regular_expression in rule["whenMatching"]:
        if rule["match_against"] == "from":
            if re.fullmatch(regular_expression, message.from_) != None:
                return True
        if rule["match_against"] == "text":
            text = message.text.strip()
            if re.fullmatch(regular_expression, text) != None:
                return True

    return False

def get_target_folder_for(message):
    for rule in config_file["rules"]:
        if is_rule_matched(rule, message):
            return rule["moveTo"]

    return None
