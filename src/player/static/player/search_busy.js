const Counter = {
    el: '#psearch',
    data() {
        return {
            show_status: true,
            players_list: [
                {
                    "account_id": 70036095,
                    "role": "combat_officer",
                    "clan_tag": "TAIRA",
                    "clan_id": 433228,
                    "last_battle_time": 1648704268,
                    "battles_in_clan_wars": 4847,
                    "nickname": "_V_3nachit_Vendetta_",
                    "stats": [
                        {
                            "tank_id": 46849,
                            "random": {
                                "avg_damage": 3504,
                                "battles": 465,
                                "percent_win": 66
                            },
                            "stronghold_defense": [{
                                "avg_damage": 2196,
                                "battles": 6,
                                "percent_win": 16
                            }],
                            "globalmap": {
                                "avg_damage": 1968,
                                "battles": 28,
                                "percent_win": 57}
                        },
                        {
                            "tank_id": 46849,
                            "random":
                                {
                                    "avg_damage": 3786,
                                    "battles": 105, "percent_win": 58
                                },
                            "stronghold_skirmish":
                                {
                                    "avg_damage": 2622,
                                    "battles": 3, "percent_win": 33
                                },
                            "stronghold_defense": [
                                    {
                                        "avg_damage": 604,
                                        "battles": 7,
                                        "percent_win": 14
                                    }],
                            "globalmap":
                                {
                                    "avg_damage": 1865,
                                    "battles": 7,
                                    "percent_win": 42
                                }
                        }
                    ]
                },
                {
                    "account_id": 14724232,
                    "role": "executive_officer",
                    "clan_tag": "TAIRA",
                    "clan_id": 433228,
                    "last_battle_time": 1648709968,
                    "battles_in_clan_wars": 762,
                    "nickname": "LokoRZD",
                    "stats": [
                        {
                            "tank_id": 46849,
                            "random":
                                {
                                    "avg_damage": 3786.980952380952,
                                    "battles": 105, "percent_win": 58.0952380952381
                                },
                            "stronghold_skirmish":
                                {
                                    "avg_damage": 2622.3333333333335,
                                    "battles": 3, "percent_win": 33.33333333333333
                                },
                            "stronghold_defense": [
                                    {
                                        "avg_damage": 604.8571428571429,
                                        "battles": 7, "percent_win": 14.285714285714285
                                    }],
                            "globalmap":
                                {
                                    "avg_damage": 1865.142857142857,
                                    "battles": 7,
                                    "percent_win": 42.857142857142854
                                }
                        }]
                },
                {"account_id": 46420137, "role": "junior_officer", "clan_tag": "TAIRA", "clan_id": 433228, "last_battle_time": 1648363968, "battles_in_clan_wars": 566, "nickname": "Mr_Kyx", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3711.364312267658, "battles": 269, "percent_win": 61.71003717472119}}]}, {"account_id": 77074648, "role": "junior_officer", "clan_tag": "TAIRA", "clan_id": 433228, "last_battle_time": 1648257678, "battles_in_clan_wars": 984, "nickname": "SOROKA_GRILb", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3724.5, "battles": 106, "percent_win": 66.0377358490566}, "globalmap": {"avg_damage": 2457.1428571428573, "battles": 7, "percent_win": 71.42857142857143}}]}, {"account_id": 20035099, "role": "combat_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648661532, "battles_in_clan_wars": 1902, "nickname": "93_n", "stats": [{"tank_id": 46849, "random": {"avg_damage": 4535.590909090909, "battles": 22, "percent_win": 59.09090909090909}, "stronghold_skirmish": {"avg_damage": 3924.0, "battles": 1, "percent_win": 0.0}}]}, {"account_id": 37015626, "role": "combat_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648381610, "battles_in_clan_wars": 4308, "nickname": "Big__Mom", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3559.8, "battles": 45, "percent_win": 62.22222222222222}, "stronghold_skirmish": {"avg_damage": 2263.733333333333, "battles": 15, "percent_win": 66.66666666666666}, "stronghold_defense": [{"avg_damage": 1789.951388888889, "battles": 144, "percent_win": 38.19444444444444}], "globalmap": {"avg_damage": 2097.6345029239765, "battles": 342, "percent_win": 66.66666666666666}}]}, {"account_id": 73495248, "role": "intelligence_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648649875, "battles_in_clan_wars": 4429, "nickname": "ToyotaTV", "stats": [{"tank_id": 46849, "random": {"avg_damage": 4133.360606060606, "battles": 330, "percent_win": 66.06060606060606}, "stronghold_skirmish": {"avg_damage": 2291.4, "battles": 5, "percent_win": 100.0}, "stronghold_defense": [{"avg_damage": 2582.5, "battles": 20, "percent_win": 35.0}], "globalmap": {"avg_damage": 2725.64, "battles": 25, "percent_win": 68.0}}]}, {"account_id": 11098860, "role": "intelligence_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648555183, "battles_in_clan_wars": 800, "nickname": "_Dark_Moon_", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3618.594017094017, "battles": 468, "percent_win": 63.67521367521367}, "globalmap": {"avg_damage": 2062.925, "battles": 80, "percent_win": 70.0}}]}, {"account_id": 31161128, "role": "intelligence_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648662386, "battles_in_clan_wars": 2558, "nickname": "ARANTIR_4CB_TOP1", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3542.260147601476, "battles": 542, "percent_win": 65.12915129151291}, "stronghold_skirmish": {"avg_damage": 1977.4, "battles": 20, "percent_win": 70.0}, "stronghold_defense": [{"avg_damage": 2577.090909090909, "battles": 11, "percent_win": 63.63636363636363}], "globalmap": {"avg_damage": 2010.2521008403362, "battles": 119, "percent_win": 59.66386554621849}}]}, {"account_id": 96000300, "role": "intelligence_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648665406, "battles_in_clan_wars": 1665, "nickname": "Mr_Banner_YT", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3996.579646017699, "battles": 226, "percent_win": 68.58407079646017}, "stronghold_skirmish": {"avg_damage": 3140.1, "battles": 10, "percent_win": 20.0}, "stronghold_defense": [{"avg_damage": 2870.5142857142855, "battles": 35, "percent_win": 48.57142857142857}], "globalmap": {"avg_damage": 2960.679069767442, "battles": 215, "percent_win": 67.44186046511628}}]}, {"account_id": 68847415, "role": "private", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648663243, "battles_in_clan_wars": 1533, "nickname": "Ridik_42ru", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3665.687752355316, "battles": 743, "percent_win": 64.06460296096904}, "stronghold_skirmish": {"avg_damage": 1919.6, "battles": 15, "percent_win": 80.0}, "stronghold_defense": [{"avg_damage": 1677.2, "battles": 5, "percent_win": 20.0}]}]}, {"account_id": 95866725, "role": "personnel_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648313704, "battles_in_clan_wars": 3600, "nickname": "BuTaMuH42", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3612.875706214689, "battles": 177, "percent_win": 56.49717514124294}, "stronghold_skirmish": {"avg_damage": 2229.1111111111113, "battles": 18, "percent_win": 55.55555555555556}, "stronghold_defense": [{"avg_damage": 2156.4606741573034, "battles": 89, "percent_win": 64.04494382022472}], "globalmap": {"avg_damage": 2374.8023255813955, "battles": 258, "percent_win": 61.627906976744185}}]}, {"account_id": 96731489, "role": "combat_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648638821, "battles_in_clan_wars": 2506, "nickname": "Butcher_of_BIaviken", "stats": [{"tank_id": 46849, "random": {"avg_damage": 4317.695652173913, "battles": 46, "percent_win": 63.04347826086957}, "stronghold_skirmish": {"avg_damage": 2368.818181818182, "battles": 22, "percent_win": 50.0}, "stronghold_defense": [{"avg_damage": 1795.2592592592594, "battles": 27, "percent_win": 44.44444444444444}], "globalmap": {"avg_damage": 1916.6272727272728, "battles": 110, "percent_win": 60.0}}]}, {"account_id": 4183431, "role": "intelligence_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648626210, "battles_in_clan_wars": 3269, "nickname": "Bogdanos", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3532.0, "battles": 24, "percent_win": 79.16666666666666}, "stronghold_skirmish": {"avg_damage": 2020.340909090909, "battles": 44, "percent_win": 65.9090909090909}, "stronghold_defense": [{"avg_damage": 2148.765625, "battles": 64, "percent_win": 40.625}], "globalmap": {"avg_damage": 1960.5935828877004, "battles": 187, "percent_win": 56.14973262032086}}]}, {"account_id": 33303027, "role": "combat_officer", "clan_tag": "SP_DV", "clan_id": 481499, "last_battle_time": 1648700300, "battles_in_clan_wars": 3898, "nickname": "6oeBou_nEJlEMEHb_HarHeT", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3592.264705882353, "battles": 34, "percent_win": 64.70588235294117}, "stronghold_skirmish": {"avg_damage": 2689.8571428571427, "battles": 7, "percent_win": 57.14285714285714}, "stronghold_defense": [{"avg_damage": 2222.25, "battles": 8, "percent_win": 62.5}], "globalmap": {"avg_damage": 2323.7083333333335, "battles": 24, "percent_win": 70.83333333333334}}]}, {"account_id": 6044291, "role": "combat_officer", "clan_tag": "SP-DW", "clan_id": 452476, "last_battle_time": 1648655469, "battles_in_clan_wars": 10441, "nickname": "creyk", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3637.126506024096, "battles": 498, "percent_win": 63.25301204819277}, "stronghold_skirmish": {"avg_damage": 1633.6666666666667, "battles": 3, "percent_win": 33.33333333333333}, "stronghold_defense": [{"avg_damage": 1584.764705882353, "battles": 17, "percent_win": 52.94117647058824}], "globalmap": {"avg_damage": 2128.6949152542375, "battles": 59, "percent_win": 66.10169491525424}}]}, {"account_id": 12980070, "role": "private", "clan_tag": "SP-DW", "clan_id": 452476, "last_battle_time": 1648655591, "battles_in_clan_wars": 1603, "nickname": "PeM6o_B_CopTupe", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3714.55, "battles": 600, "percent_win": 63.66666666666667}, "stronghold_skirmish": {"avg_damage": 2612.4444444444443, "battles": 9, "percent_win": 33.33333333333333}, "stronghold_defense": [{"avg_damage": 1289.0, "battles": 3, "percent_win": 0.0}], "globalmap": {"avg_damage": 2189.159090909091, "battles": 44, "percent_win": 43.18181818181818}}]}, {"account_id": 1545592, "role": "private", "clan_tag": "SP-DW", "clan_id": 452476, "last_battle_time": 1648667259, "battles_in_clan_wars": 10034, "nickname": "TeJIenopT", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3913.967320261438, "battles": 153, "percent_win": 75.16339869281046}, "stronghold_skirmish": {"avg_damage": 1870.9238095238095, "battles": 105, "percent_win": 66.66666666666666}, "stronghold_defense": [{"avg_damage": 1896.59375, "battles": 32, "percent_win": 40.625}], "globalmap": {"avg_damage": 1678.6125, "battles": 80, "percent_win": 71.25}}]}, {"account_id": 14713768, "role": "intelligence_officer", "clan_tag": "SP-DW", "clan_id": 452476, "last_battle_time": 1648328663, "battles_in_clan_wars": 5379, "nickname": "OTKp0u_COBA_nPuLLIJIa", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3868.3, "battles": 100, "percent_win": 65.0}, "stronghold_defense": [{"avg_damage": 2351.0, "battles": 26, "percent_win": 61.53846153846154}], "globalmap": {"avg_damage": 1920.4615384615386, "battles": 26, "percent_win": 61.53846153846154}}]}, {"account_id": 319935, "role": "combat_officer", "clan_tag": "SP-DW", "clan_id": 452476, "last_battle_time": 1648293083, "battles_in_clan_wars": 995, "nickname": "Doberman_pro", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3763.093023255814, "battles": 559, "percent_win": 64.22182468694096}, "stronghold_skirmish": {"avg_damage": 1823.2142857142858, "battles": 14, "percent_win": 28.57142857142857}, "stronghold_defense": [{"avg_damage": 1596.24, "battles": 25, "percent_win": 56.00000000000001}], "globalmap": {"avg_damage": 2456.729442970822, "battles": 377, "percent_win": 61.273209549071616}}]}, {"account_id": 5475277, "role": "recruitment_officer", "clan_tag": "SP-DW", "clan_id": 452476, "last_battle_time": 1648665543, "battles_in_clan_wars": 6216, "nickname": "Markelof123", "stats": [{"tank_id": 46849, "random": {"avg_damage": 3669.0290556900727, "battles": 413, "percent_win": 63.438256658595634}, "stronghold_skirmish": {"avg_damage": 1908.9285714285713, "battles": 14, "percent_win": 78.57142857142857}, "stronghold_defense": [{"avg_damage": 2223.2616822429904, "battles": 107, "percent_win": 51.4018691588785}], "globalmap": {"avg_damage": 2296.9761904761904, "battles": 42, "percent_win": 76.19047619047619}}]}, {"account_id": 16825840, "role": "recruit", "clan_tag": "SP-DW", "clan_id": 452476, "last_battle_time": 1648547538, "battles_in_clan_wars": 2278, "nickname": "Piece_of_sh1t", "stats": [{"tank_id": 46849, "random": {"avg_damage": 4820.847107438017, "battles": 242, "percent_win": 70.24793388429752}, "globalmap": {"avg_damage": 3395.5, "battles": 2, "percent_win": 50.0}}]}]
        }
    }
};

Vue.createApp(Counter).mount('#psearch')