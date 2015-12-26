
def flatten_match (match):

    match_as_array = []

    match_as_array.append(match["radiant_win"])
    match_as_array.append(match["start_time"])
    match_as_array.append(match["duration"])
    match_as_array.append(match["tower_status_radiant"])
    match_as_array.append(match["tower_status_dire"])
    match_as_array.append(match["barracks_status_radiant"])
    match_as_array.append(match["barracks_status_dire"])
    match_as_array.append(match["cluster"])
    match_as_array.append(match["first_blood_time"])
    match_as_array.append(match["lobby_type"])
    match_as_array.append(match["human_players"])
    match_as_array.append(match["game_mode"])
    match_as_array.append(match["cluster"])
    match_as_array.append(match["cluster"])
    match_as_array.append(match["cluster"])

    players = match["players"]
    for player in players:

        match_as_array.append(player["hero_id"])
        match_as_array.append(player["item_0"])
        match_as_array.append(player["item_1"])
        match_as_array.append(player["item_2"])
        match_as_array.append(player["item_3"])
        match_as_array.append(player["item_4"])
        match_as_array.append(player["item_5"])
        match_as_array.append(player["kills"])
        match_as_array.append(player["deaths"])
        match_as_array.append(player["assists"])
        match_as_array.append(player["leaver_status"])
        match_as_array.append(player["gold"])
        match_as_array.append(player["last_hits"])
        match_as_array.append(player["denies"])
        match_as_array.append(player["gold_per_min"])
        match_as_array.append(player["xp_per_min"])
        match_as_array.append(player["gold_spent"])
        match_as_array.append(player["hero_damage"])
        match_as_array.append(player["tower_damage"])
        match_as_array.append(player["hero_healing"])
        match_as_array.append(player["level"])
        match_as_array.append(player["stuns"])
        match_as_array.append(len(player["obs_log"]))
        match_as_array.append(len(player["sen_log"]))
        match_as_array.append(len(player["purchase_log"]))
        match_as_array.append(len(player["buyback_log"]))

        def test_over_array (dict, array):
            for i in array:
                match_as_array.append(dict[str(i)] if str(i) in dict else 0)

        def test_over_range (dict, min_val, max_val):
            test_over_array(dict, range(min_val, max_val + 1))

        test_over_range(player["actions"], 0, 28)

        test_over_range(player["pings"], 0, 0)

        test_over_array(player["purchase"], ["courier", "branches", \
                "circlet", "clarity", "tango", "tpscroll", \
                "smoke_of_deceit", "magic_stick", "magic_wand"])

        test_over_range(player["gold_reasons"], 0, 15)

        test_over_range(player["xp_reasons"], 0, 3)

        match_as_array.append(len(player["runes"]))

        test_over_range(player["kill_streaks"], 3, 10)

        test_over_range(player["multi_kills"], 2, 5)

    return match_as_array
