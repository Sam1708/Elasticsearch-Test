import csv

def generate_csv(num_records):
    # Define the column names
    field_names = ['ID', 'Name', 'Team', 'Score', 'Matches_Played', 'Goals', 'Assists', 'Yellow_Cards', 'Red_Cards']
    
    # Create the CSV file and write the header
    with open('generated_sports_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        
        # Generate the data for each record
        for i in range(1, num_records+1):
            name = f'Player {i % 10 + 1}'
            team = f'Team {i % 5 + 1}'
            score = i % 20
            matches_played = i % 10 + 1
            goals = i % 5
            assists = i % 3
            yellow_cards = i % 2
            red_cards = i % 2
            
            # Write the data for the current record to the CSV file
            writer.writerow({
                'ID': i,
                'Name': name,
                'Team': team,
                'Score': score,
                'Matches_Played': matches_played,
                'Goals': goals,
                'Assists': assists,
                'Yellow_Cards': yellow_cards,
                'Red_Cards': red_cards
            })
            
    print(f'{num_records} records generated successfully.')

# Call the function with the desired number of records
generate_csv(10000)
