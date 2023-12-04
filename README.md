# Office Reservation Revenue Analysis

This Python script calculates the monthly revenue and total capacity of unreserved offices based on reservation data. It reads a CSV file containing office reservation details and computes the revenue for a specified month and year, accounting for partial reservations. It also calculates the total capacity of offices that are not reserved for the specified month.

## Prerequisites

Before running the script, ensure you have the following prerequisites installed:
- Python (version 3.x)
- `pandas` library (for data manipulation and analysis)

## Installation

1. **Clone the Repository**
   
   Clone this repository to your local machine using:

```
    git clone https://github.com/razvan233/kaltura-assigment.git
```


2. **Install Required Packages**

Navigate to the cloned repository's directory and install the required packages using:

```
    pip install -r req.txt
```


## Usage

1. **Prepare the Data**

Ensure your CSV file with office reservation data is in the same directory as the script or update the script with the correct path to your CSV file. The CSV file should have the following columns: `Capacity`, `Monthly Price`, `Start Day`, `End Day`.

2. **Run the Script**

Run the script from the command line:

```
    python main.py
```

3. **Enter Dates**

When prompted, enter the date in `YYYY-MM` format for which you want to calculate the revenue and capacity. For example, `2014-12`. To exit the program, type `exit`.

## Output

The script outputs the expected revenue and the total capacity of unreserved offices for the entered month and year, formatted as follows:

```
    2014-12: expected revenue: $9,363, expected total capacity of the unreserved offices: 135
```