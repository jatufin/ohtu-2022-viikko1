import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_asettaa_negatiivisen_tilavuuden_nollaksi(self):
        virheellinen_varasto = Varasto(-1)
        self.assertAlmostEqual(virheellinen_varasto.tilavuus, 0)

    def test_konstruktori_asettaa_negatiivisen_saldon_nollaksi(self):
        virheellinen_varasto = Varasto(10, alku_saldo=-1)
        self.assertAlmostEqual(virheellinen_varasto.saldo, 0)
        
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.saldo, 0)
        
    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_tilavuuden_yli_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)
        
        self.assertAlmostEqual(self.varasto.saldo, 10)
        
    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_negatiivisen_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_yli_saldon_ottaminen_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(saatu_maara, 8)
        
    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_str_palauttaa_oikean_merkkijono(self):
        self.varasto.lisaa_varastoon(8)

        s = str(self.varasto)

        self.assertEqual(s, "Xsaldo = 8, vielä tilaa 2")
                
