"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""


def main():
    """Run the HarborFlow Dispatch Console."""
    # TODO: implement the persistent menu and dispatch to task functions.
    pass


#validate a booking reference
def validate_ref(reference):

    reference = input("Enter booking reference: ")
    result_cleaned = reference.strip().upper()
    if len(result_cleaned) != 12:
        return ""
    if result_cleaned[3] != "-" or result_cleaned[7] != "-":
        return ""
    prefix = result_cleaned[0:3]
    customer_code = result_cleaned[4:7]
    shipment_number = result_cleaned[8:12]
    if prefix != "HFL":
        return "Please enter a valid booking reference (HFL-XXX-YYYY)."
    if len(customer_code) != 3 or not customer_code.isalpha():
        return "Please enter a valid customer code (3 letters)."
    if len(shipment_number) != 4 or not shipment_number.isdigit():
        return "Please enter a valid shipment number (4 digits)."
    
    return result_cleaned