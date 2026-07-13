class AnalysisFilter:

    @staticmethod
    def opportunities(analyses):

        return [
            analysis
            for analysis in analyses
            if analysis["recommendation"] != "SKIP"
        ]