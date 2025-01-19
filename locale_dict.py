class LocaleParser():
    def __init__(self):

        self.dict = {}

    def locale(self, choice):

        self.dict = {
            "en-US": "www.trustpilot.com",
            "de-AT": "at.trustpilot.com",
            "en-AU": "au.trustpilot.com",
            "pt-BR": "br.trustpilot.com",
            "en-CA": "ca.trustpilot.com",
            "de-CH": "ch.trustpilot.com",
            "de-DE": "de.trustpilot.com",
            "da-DK": "dk.trustpilot.com",
            "es-ES": "es.trustpilot.com",
            "fi-FI": "fi.trustpilot.com",
            "fr-FR": "fr.trustpilot.com",
            "fr-BE": "fr-be.trustpilot.com",
            "en-IE": "ie.trustpilot.com",
            "it-IT": "it.trustpilot.com",
            "ja-JP": "jp.trustpilot.com",
            "nl-NL": "nl.trustpilot.com",
            "nl-BE": "nl-be.trustpilot.com",
            "nb-NO": "no.trustpilot.com",
            "en-NZ": "nz.trustpilot.com",
            "pl-PL": "pl.trustpilot.com",
            "pt-PT": "pt.trustpilot.com",
            "sv-SE": "se.trustpilot.com",
            "en-GB": "uk.trustpilot.com"
        }

        return self.dict[choice]