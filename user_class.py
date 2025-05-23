import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class User:
    def __init__(self, csv_file='survey_data.csv'):
        """Load survey data from CSV file"""
        try:
            self.data = pd.read_csv(csv_file)
            print(f"✅ Loaded {len(self.data)} survey responses")
        except FileNotFoundError:
            print("❌ No CSV file found. Please export data first.")
            self.data = pd.DataFrame()

    def analyze_age_income(self):
        """Show ages with highest income"""
        if self.data.empty:
            return "No data available"

        # Group by age and calculate average income
        age_income = self.data.groupby('age')['total_income'].mean().sort_values(ascending=False)

        print("📊 AGES WITH HIGHEST INCOME:")
        print("-" * 30)
        for age, income in age_income.head(10).items():
            print(f"Age {age}: ${income:,.0f}")

        return age_income

    def analyze_gender_spending(self):
        """Show gender distribution across spending categories"""
        if self.data.empty:
            return "No data available"

        categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']

        print("\n👥 GENDER SPENDING PATTERNS:")
        print("-" * 30)

        for category in categories:
            print(f"\n{category.upper()}:")
            gender_spending = self.data.groupby('gender')[category].mean()
            for gender, amount in gender_spending.items():
                print(f"  {gender}: ${amount:,.0f}")

        return self.data.groupby('gender')[categories].mean()

    def create_charts(self):
        """Create the required visualizations"""
        if self.data.empty:
            print("❌ No data to create charts")
            return

        # Chart 1: Ages with highest income
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        age_income = self.data.groupby('age')['total_income'].mean().sort_values(ascending=False).head(10)
        age_income.plot(kind='bar', color='skyblue')
        plt.title('Ages with Highest Income')
        plt.xlabel('Age')
        plt.ylabel('Average Income ($)')
        plt.xticks(rotation=45)

        # Chart 2: Gender spending distribution
        plt.subplot(1, 2, 2)
        categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
        gender_data = self.data.groupby('gender')[categories].mean()
        gender_data.plot(kind='bar', stacked=True)
        plt.title('Gender Distribution Across Spending Categories')
        plt.xlabel('Gender')
        plt.ylabel('Average Spending ($)')
        plt.xticks(rotation=45)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.tight_layout()
        plt.savefig('survey_charts.png', dpi=300, bbox_inches='tight')
        plt.show()

        print("✅ Charts saved as 'survey_charts.png'")

    def summary_report(self):
        """Generate a summary report"""
        if self.data.empty:
            return "No data available"

        print("\n📋 SURVEY SUMMARY REPORT")
        print("=" * 50)
        print(f"Total Responses: {len(self.data)}")
        print(f"Average Age: {self.data['age'].mean():.1f}")
        print(f"Average Income: ${self.data['total_income'].mean():,.0f}")

        # Top spending category
        categories = ['utilities', 'entertainment', 'school_fees', 'shopping', 'healthcare']
        total_spending = self.data[categories].sum()
        top_category = total_spending.idxmax()
        print(f"Top Spending Category: {top_category} (${total_spending[top_category]:,.0f} total)")

        return {
            'total_responses': len(self.data),
            'avg_age': self.data['age'].mean(),
            'avg_income': self.data['total_income'].mean(),
            'top_category': top_category
        }


# Example usage
if __name__ == "__main__":
    print("🔍 Healthcare Survey Data Analysis")
    print("-" * 40)

    # Create User object
    user = User()

    # Run analyses
    user.analyze_age_income()
    user.analyze_gender_spending()
    user.summary_report()
    user.create_charts()