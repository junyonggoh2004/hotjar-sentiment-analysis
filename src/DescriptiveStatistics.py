class DescriptiveStatistics:
    def __init__(self, df):
        self.df = df        
    
    def get_df_len(self):
        return f"There are currently {len(self.df)} survey responses."

    def get_df_date_range(self):
        return f"Data Collected from {self.df['Date Submitted'].min()} to {self.df['Date Submitted'].max()}"

    def get_df_head(self):
        return f"Dataset Sample:\n{self.df.head()}"
    
    def get_unique_user_count(self):
        return f"Number of Unique Users:\n{len(self.df['User'].unique())}"
        
    def get_response_count_by_hotel(self):
        response_counts = self.df['Hotel'].value_counts().reset_index()
        result = [
            f"{x}: {y}"
            for x, y in zip(
                response_counts['Hotel'].tolist(),
                response_counts['count'].tolist(),
            )
        ]
        return "Number of Responses by Hotel:\n" + ", ".join(result)

    def get_top_response_count_by_country(self):
        country_counts = self.df['Country'].value_counts().reset_index()[:3]
        result = [
            f"{x}: {y}"
            for x, y in zip(
                country_counts['Country'].tolist(),
                country_counts['count'].tolist(),
            )
        ]
        return "Number of Top Responses by Country:\n" + ", ".join(result)

    def run_descriptive_statistics(self):
        results = [
            self.get_df_date_range(),
            self.get_df_head(),
            self.get_df_len(),
            self.get_top_response_count_by_country(),
            self.get_response_count_by_hotel(),
            self.get_unique_user_count(),
        ]
        return "\n\n".join(results)
