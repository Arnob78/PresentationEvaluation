import pandas as pd
import datetime

# Create an empty DataFrame to store the evaluation scores
df = pd.DataFrame(columns=['Date', 'Time', 'Presenter', 'Evaluator', 'Category1', 'Category2', 'Category3', 'Category4', 'Category5'])

# Define the list of evaluators
evaluators = ['Evaluator1', 'Evaluator2', 'Evaluator3', 'Evaluator4', 'Evaluator5', 'Evaluator6']

# Define the list of categories
categories = ['Category1', 'Category2', 'Category3', 'Category4', 'Category5']

# Define the presentation details
presenters = ['Presenter1', 'Presenter2', 'Presenter3', 'Presenter4', 'Presenter5', 'Presenter6']
presentation_date = datetime.date(2023, 6, 27)

# Define the time slots for presentations
time_slots = pd.date_range(start='09:00', end='17:00', freq='15min')

# Iterate over the time slots and presenters to create evaluation records
for time_slot in time_slots:
    for presenter in presenters:
        evaluator_scores = []
        
        # Get evaluator scores for each category
        for evaluator in evaluators:
            print("Presentation Date:", presentation_date)
            print("Time Slot:", time_slot.time())
            print("Presenter:", presenter)
            print("Evaluator:", evaluator)
            
            # Prompt the evaluator to enter scores for each category
            scores = []
            for category in categories:
                score = int(input(f"Enter {category} score (1-10): "))
                scores.append(score)
            
            # Add the evaluation record to the DataFrame
            df.loc[len(df)] = [presentation_date, time_slot.time(), presenter, evaluator] + scores
        
        print("Evaluation completed for Presenter:", presenter)
        print("=" * 50)

# Save the evaluation data to a CSV file
df.to_csv('evaluation_scores.csv', index=False)
