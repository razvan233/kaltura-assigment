import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    return df


def parse_dates(df):
    df['Start Day'] = pd.to_datetime(df['Start Day'], errors='coerce')
    df['End Day'] = pd.to_datetime(df['End Day'], errors='coerce')
    return df


def calculate_revenue_and_capacity(df, year, month):
    start_of_month = pd.Timestamp(year, month, 1)
    if month == 12:
        end_of_month = pd.Timestamp(year, month, 31)
    else:
        end_of_month = pd.Timestamp(year, month + 1, 1) - pd.Timedelta(days=1)


    total_revenue = 0
    total_capacity = 0

    for index, row in df.iterrows():
        start = row['Start Day']
        end = row['End Day'] if pd.notna(
            row['End Day']) else end_of_month + pd.Timedelta(days=1)

        if start <= end_of_month and end >= start_of_month:
            days_in_month = (min(end, end_of_month) -
                             max(start, start_of_month)).days + 1
            days_reserved = (end - start).days + 1
            revenue = (row['Monthly Price'] / days_reserved) * days_in_month
            total_revenue += revenue
        else:
            total_capacity += row['Capacity']

    return total_revenue, total_capacity

def test_script(df):
    for year_month in ['2013-01', '2013-06', '2014-03', '2014-09', '2015-07']:
        year, month = map(int, year_month.split('-'))
        revenue, capacity = calculate_revenue_and_capacity(df, year, month)
        print(f"{year_month}: expected revenue: ${revenue:,.0f}, expected total capacity of the unreserved offices: {capacity}")

def main():
    file_path = 'data.csv'
    df = load_data(file_path)
    df = parse_dates(df)
    test_script(df)
    while True:
        year_month = input("Enter a date in YYYY-MM format (or type 'exit' to quit): ")
        if year_month.lower() == 'exit':
            break

        try:
            year, month = map(int, year_month.split('-'))
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")
            revenue, capacity = calculate_revenue_and_capacity(df, year, month)
            print(f"{year_month}: expected revenue: ${revenue:,.0f}, expected total capacity of the unreserved offices: {capacity}")
        except ValueError as e:
            print(f"Invalid input: {e}")

    


if __name__ == "__main__":
    main()
