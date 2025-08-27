# gestion_des_agences.py

CHOIX_DE_L_AGENCE = {}
# Correspondances pour l'agence d'Arras
CORRESPONDANCES_ARRAS = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
    # A verfier si valeur ok
    '1525': 'à Payer  ',
}

rubriques_en_doublon_ARRAS = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_ARRAS = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_ARRAS = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_ARRAS = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence d'Asnières
CORRESPONDANCES_ASNIERES = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_ASNIERES = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_ASNIERES = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_ASNIERES = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_ASNIERES = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de BETHUNE
CORRESPONDANCES_BETHUNE = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1172': 'Base   ',
    '1175': 'Base   ',
    '1285': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3212': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_BETHUNE = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_BETHUNE = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_BETHUNE = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_BETHUNE = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de CARVIN
CORRESPONDANCES_CARVIN = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1202': 'Base   ',
    '1235': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'à Retenir  ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_CARVIN = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_CARVIN = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_CARVIN = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_CARVIN = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

CORRESPONDANCES_CHARLEVILLE = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1190': 'Base   ',
    '1191': 'Base   ',
    '1192': 'Base   ',
    '1201': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_CHARLEVILLE = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_CHARLEVILLE = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_CHARLEVILLE = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_CHARLEVILLE = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

CORRESPONDANCES_CRETEIL = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1445': 'Mont_Base ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3102': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5101': 'à Retenir  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_CRETEIL = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_CRETEIL = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_CRETEIL = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_CRETEIL = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de Douai
CORRESPONDANCES_DOUAI = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1191': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3082': 'Patronal Mont',
	
    '3083': 'Base   ',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_DOUAI = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_DOUAI = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_DOUAI = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_DOUAI = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de DUNKERQUE
CORRESPONDANCES_DUNKERQUE = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_DUNKERQUE = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_DUNKERQUE = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_DUNKERQUE = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_DUNKERQUE = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence d'Essonne
CORRESPONDANCES_ESSONNE = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
# A verfier si valeur ok
    '1235': 'Base   ',
# A verfier si valeur ok
    '1300': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_ESSONNE = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_ESSONNE = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_ESSONNE = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_ESSONNE = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de Lens
CORRESPONDANCES_LENS = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1500': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'à Retenir  ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_LENS = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_LENS = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_LENS = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_LENS = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de LESQUIN
CORRESPONDANCES_LESQUIN = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1172': 'Base   ',
    '1175': 'Base   ',
    '1191': 'Base   ',
    '1340': 'Base   ',
    '1420': 'Base   ',
    '1425': 'Base   ',
    '1540': 'Base   ',
    '1545': 'Base   ',
    '1550': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_LESQUIN = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_LESQUIN = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_LESQUIN = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_LESQUIN = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de LILLE ENV.
CORRESPONDANCES_LILLEENVIRONNEMENT = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1206': 'Base   ',
    '1425': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'à Retenir  ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_LILLEENVIRONNEMENT = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_LILLEENVIRONNEMENT = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_LILLEENVIRONNEMENT = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_LILLEENVIRONNEMENT = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de LILLE GENERALISTE
CORRESPONDANCES_LILLEGENERALISTE = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1206': 'Base   ',
    '1425': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'à Retenir  ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_LILLEGENERALISTE = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '5110': ['5110', '5110 base', '5110 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_LILLEGENERALISTE = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_LILLEGENERALISTE = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_LILLEGENERALISTE = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

CORRESPONDANCES_MAUBEUGE = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1525': 'à Payer  ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3083': 'Mont_Base ',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_MAUBEUGE = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_MAUBEUGE = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_MAUBEUGE = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_MAUBEUGE = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de MONTEVRAIN
CORRESPONDANCES_MONTEVRAIN = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    # A Controler:
    '1202': 'Base   ',
    # A Controler:
    '1235': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_MONTEVRAIN = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_MONTEVRAIN = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_MONTEVRAIN = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_MONTEVRAIN = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de PARIS
CORRESPONDANCES_PARIS = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    # A Controler
    '5101': 'à Retenir  ',
    # A Controler
   # '5110': 'à Retenir  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_PARIS = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '5110': ['5110', '5110 base', '5110 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_PARIS = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_PARIS = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_PARIS = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}


# Correspondances pour l'agence de ROUBAIX
CORRESPONDANCES_ROUBAIX = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_ROUBAIX = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_ROUBAIX = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_ROUBAIX = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_ROUBAIX = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de VALENCIENNES
CORRESPONDANCES_VALENCIENNES = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    # A controler
    '1172': 'Base   ',
    '1175': 'Base   ',
    # A controler
    '1285': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
	#rajouté par Dom
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
	#
    '3211': 'Mont_Base ',
    '3212': 'Mont_Base ',
    '3218': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'Base   ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_VALENCIENNES = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_VALENCIENNES = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_VALENCIENNES = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_VALENCIENNES = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Correspondances pour l'agence de VILLEPINTE
CORRESPONDANCES_VILLEPINTE = {
    '1110': 'Base   ',
    '1120': 'Base   ',
    '1130': 'Base   ',
    '1170': 'Base   ',
    '1175': 'Base   ',
    '1202': 'Base   ',
    '1235': 'Base   ',
    '1900': 'à Payer  ',
    '1910': 'à Payer  ',
    '3005': 'Mont_Base ',
    '3006': 'Mont_Base ',
    '3007': 'Mont_Base ',
    '3031': 'Patronal Mont',
    '3050': 'Patronal Mont',
    '3081': 'Patronal Mont',
    '3101': 'Mont_Base ',
    '3201': 'Mont_Base ',
    '3202': 'Mont_Base ',
    '3208': 'Mont_Base ',
    '3401': 'Mont_Base ',
    '3402': 'Mont_Base ',
    '3403': 'Mont_Base ',
    '3404': 'Mont_Base ',
    '3601': 'Mont_Base ',
    '3750': 'Mont_Base ',
    '4072': 'à Payer  ',
    '5230': 'à Retenir  ',
    '6000': 'à Retenir  ',
    '6011': 'à Retenir  ',
}

rubriques_en_doublon_VILLEPINTE = {
    '3082': ['3082', '3082 base', '3082 patronal montant'],
    '5100': ['5100', '5100 base', '5100 à retenir'],
    '5102': ['5102', '5102 base', '5102 à retenir'],
    '5103': ['5103', '5103 base', '5103 à retenir'],
    '3602': ['3602', '3602 base', '3602 à retenir'],
    '4076': ['4076', '4076 base', '4076 à payer'],
}
rubriques_en_doublon_2_VILLEPINTE = {
    '3082 base': 'Mont_Base ',
    '3082 patronal montant': 'Patronal Mont',
    '5100 base': 'Mont_Base ',
    '5100 à retenir': 'à Retenir  ',
    '5102 base': 'Mont_Base ',
    '5102 à retenir': 'à Retenir  ',
    '5103 base': 'Mont_Base ',
    '5103 à retenir': 'à Retenir  ',
    '3602 base': 'Mont_Base ',
    '3602 à retenir': 'à Retenir  ',
    '4076 base': 'Mont_Base ',
    '4076 à payer': 'à Payer  ',
}

rubriques_en_triplon_VILLEPINTE = {
    '5110': ['5110 base', '5110 salarié montant', '5110 à retenir'],
}
rubriques_en_triplon_2_VILLEPINTE = {
    '5110 base': 'Mont_Base ',
    '5110 salarié montant': 'Salarié Mont',
    '5110 à retenir' : 'à Retenir  ',
}

# Dictionnaire principal contenant toutes les correspondances pour chaque agence
CORRESPONDANCES_AGENCES = {
    'Choix de l agence' : CHOIX_DE_L_AGENCE,
    'ARRAS': CORRESPONDANCES_ARRAS,
    'ASNIERES': CORRESPONDANCES_ASNIERES,
    'BETHUNE': CORRESPONDANCES_BETHUNE,
    'CARVIN': CORRESPONDANCES_CARVIN,
    'CHARLEVILLE': CORRESPONDANCES_CHARLEVILLE,
    'CRETEIL': CORRESPONDANCES_CRETEIL,
    'DOUAI': CORRESPONDANCES_DOUAI,
    'DUNKERQUE': CORRESPONDANCES_DUNKERQUE,
    'ESSONNE': CORRESPONDANCES_ESSONNE,
    'LENS': CORRESPONDANCES_LENS,
    'LESQUIN': CORRESPONDANCES_LESQUIN,
    'LILLEENVIRONNEMENT': CORRESPONDANCES_LILLEENVIRONNEMENT,
    'LILLEGENERALISTE': CORRESPONDANCES_LILLEGENERALISTE,
    'MAUBEUGE': CORRESPONDANCES_MAUBEUGE,
    'MONTEVRAIN': CORRESPONDANCES_MONTEVRAIN,
    'PARIS': CORRESPONDANCES_PARIS,
    'ROUBAIX': CORRESPONDANCES_ROUBAIX,
    'VALENCIENNES': CORRESPONDANCES_VALENCIENNES,
    'VILLEPINTE': CORRESPONDANCES_VILLEPINTE,
}
