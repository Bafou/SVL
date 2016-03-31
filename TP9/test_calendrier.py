"""
Antoine PETIT & Sarah Wissocq
Test calendrier
"""

import unittest

from hypothesis import given, assume, example
from hypothesis.strategies import *

from calendrier import *


class TestEstBissextile(unittest.TestCase):

	@given(annee= integers(min_value=1))
	@example(annee=400)
	def test_divisible_par_4_mais_pas_par_100_mais_par_400_est_bissextile(self, annee):
		cal = Calendrier()
		assume((annee % 400 == 0) or ((annee % 4 == 0) and (annee % 100 != 0)))
		self.assertTrue(cal.est_bissextile(annee))

	@given(annee= integers(min_value=1))
	def test_divisible_par_4_mais_pas_par_100_mais_par_400_est_pas_bissextile(self, annee):
		cal = Calendrier()
		assume(not ((annee % 400 == 0) or ((annee % 4 == 0) and (annee % 100 != 0))))
		self.assertFalse(cal.est_bissextile(annee))

	@given(annee= integers(min_value=1))
	def test_annee_qui_suit_une_annee_bissextile_n_est_pas_bissextile(self, annee):
		cal = Calendrier()
		assert not (cal.est_bissextile(annee) and cal.est_bissextile(annee +1))

	@given(annee=integers(max_value=0))
	def test_echec_si_annee_negative_echec(self, annee):
		cal = Calendrier()
		self.assertRaises(ValueError,
							cal.est_bissextile,
							annee)

class TestNbJourMois(unittest.TestCase):

	@given(annee= integers(min_value=1), mois= integers(min_value=1, max_value=12))
	def test_nb_jours_mois_egal_a_31(self,mois,annee):
		cal = Calendrier()
		assume(mois==1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois ==12)
		self.assertEquals(31, cal.nb_jour(mois,annee))

	@given(annee= integers(min_value=1), mois= integers(min_value=1, max_value=12))
	def test_nb_jours_mois_egal_a_30(self,mois,annee):
		cal = Calendrier()
		assume(mois == 4 or mois == 6 or mois == 9 or mois == 11)
		self.assertEquals(30, cal.nb_jour(mois,annee))

	@given(annee= integers(min_value=1))
	def test_nb_jours_mois_fevrier_bissextile(self,annee):
		cal = Calendrier()
		assume(cal.est_bissextile(annee))
		self.assertEquals(29, cal.nb_jour(2,annee))

	@given(annee= integers(min_value=1))
	def test_nb_jours_mois_fevrier_non_bissextile(self,annee):
		cal = Calendrier()
		assume(not cal.est_bissextile(annee))
		self.assertEquals(28, cal.nb_jour(2,annee))

	@given(mois =integers(min_value=1, max_value=12), annee=integers(max_value=0))
	def test_echec_si_annee_negative_echec(self, mois,  annee):
		cal = Calendrier()
		self.assertRaises(ValueError,
							cal.nb_jour,
							mois,
							annee)

	@given(mois =integers(max_value=0), annee=integers(min_value=1))
	def test_echec_si_mois_negatif_echec(self, mois,  annee):
		cal = Calendrier()
		self.assertRaises(ValueError,
							cal.nb_jour,
							mois,
							annee)

	@given(mois =integers(min_value=13), annee=integers(min_value=1))
	def test_echec_si_mois_superieur_a_12_echec(self, mois,  annee):
		cal = Calendrier()
		self.assertRaises(ValueError,
							cal.nb_jour,
							mois,
							annee)

	@given(annee= integers(min_value=1), mois= integers(min_value=1, max_value=12))		
	def test_apres_mois_30_jours_on_a_mois_31_jours(self, mois, annee):
		cal = Calendrier()
		self.assertFalse(cal.nb_jour(mois, annee) == 30 and cal.nb_jour(mois+1, annee) != 31)

	@given(annee= integers(min_value=1), mois= integers(min_value=1, max_value=12))		
	def test_avant_mois_30_jours_on_a_mois_31_jours(self, mois, annee):
		cal = Calendrier()
		self.assertFalse(cal.nb_jour(mois, annee) == 30 and cal.nb_jour(mois-1, annee) != 31)


class TestDateValide(unittest.TestCase):

	@given(annee= integers(min_value=1), mois = integers(min_value=1, max_value= 12), jour = integers(min_value= 1,max_value =28))
	def test_date_valide_pour_jour_compris_entre_1_et_28(self,jour,mois,annee):
		cal = Calendrier()
		self.assertTrue(cal.date_valide(jour,mois,annee))

	@given(annee= integers(min_value=1), mois = integers(min_value=1, max_value=12), jour = integers(max_value =0))
	def test_date_non_valide_si_jour_negatif(self,jour,mois,annee):
		cal = Calendrier()
		self.assertFalse(cal.date_valide(jour,mois,annee))

	@given(annee= integers(min_value=1), mois = integers(min_value=13), jour = integers(min_value= 1,max_value =28))
	def test_date_non_valide_pour_mois_plus_grand_que_13(self,jour,mois,annee):
		cal = Calendrier()
		self.assertFalse(cal.date_valide(jour,mois,annee))


	@given(annee= integers(min_value=1), mois = integers(max_value=0), jour = integers(min_value= 1,max_value =28))
	def test_date_non_valide_pour_mois_negatif(self,jour,mois,annee):
		cal = Calendrier()
		self.assertFalse(cal.date_valide(jour,mois,annee))

	@given(annee= integers(max_value=0), mois = integers(min_value=1, max_value=12), jour = integers(min_value= 1,max_value =28))
	def test_date_non_valide_pour_annee_negative(self,jour,mois,annee):
		cal = Calendrier()
		self.assertFalse(cal.date_valide(jour,mois,annee))


class TestNumeroJourSemaine(unittest.TestCase):

	@given(annee= integers(min_value=1), mois = integers(min_value=1, max_value= 12), jour = integers(min_value= 1,max_value =31))
	def test_jour_suivant_d_un_jour_dans_un_mois_est_le_jour_suivant_dans_la_semaine(self,jour,mois,annee):
		cal = Calendrier()
		assume(cal.date_valide(jour, mois ,annee) and cal.date_valide(jour+1, mois, annee))
		self.assertFalse ((cal.numero_jour_semaine(jour, mois, annee) +1 % 7) == cal.numero_jour_semaine(jour+1, mois, annee))
		
