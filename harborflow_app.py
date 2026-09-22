"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""


def main():
       """Run the HarborFlow Dispatch Console."""
    # TODO: implement the persistent menu and dispatch to task functions.

    menychoice = "0"
    van_capacity_str = "0"
    van_capacity_int = 0
    remaining_capacity = 0
    parcel_weight_str = "0"
    parcel_weights_list = []
    accepted_parcels = 0
   
    print("HARBORFLOW DISPATCH CONSOLE")
    print("1. Close console")
    print("2. Validate booking reference")
    print("3. Calculate delivery quote")
    print("4. Consolidate parcel labels")
    print("5. Check van capacity")
    print("6. Classify service performance")
    print("7. Produce weekly dispatch report")

    while menychoice != "1":

     menychoice = input("Select service: ")

     if menychoice == "1":
        print("Console closed. Dispatch data remains safe.")
        break
     
     elif menychoice == "2":
        """Task 2"""

     elif menychoice == "3":
        """Task 3"""         


     elif menychoice == "4":
        """Task 4"""

     elif menychoice == "5":

        van_capacity_int = 0

        while van_capacity_int <= 0:
         van_capacity_str = input("Plesse enter the van capacity (kg): ")
         if van_capacity_str.isnumeric() == True:
            van_capacity_int = int(van_capacity_str)
         else:
          print("Error - Value must be a possitve integer")
         if van_capacity_int <= 0:
            print("Error - Value must be greater than zero.")

        #
        while parcel_weight_str != "run":
           parcel_weight_str = input("Please add a parcel (kg) or type 'run' to run the program: ")
           if parcel_weight_str.isnumeric() == True:
              if int(parcel_weight_str) > 0:
               parcel_weights_list.append(int(parcel_weight_str))
              else:
                 print("Error - Value must be greater than zero or type run to 'run' the program")

        print(f"Van capacity (kg): {van_capacity_int}")
        remaining_capacity = van_capacity_int
        temp_range = len(parcel_weights_list)
        print(remaining_capacity)

        #Calculates the remaing capacity by going through the list of weights and subtracting the values
        # that are lower than the remaining capacity from the capacity
        for i in range(0, temp_range):
           if remaining_capacity - parcel_weights_list[i] >= 0:  
              remaining_capacity = remaining_capacity - parcel_weights_list[i]            
              accepted_parcels += 1
              print(f"Parcel {i+1}: Accepted")
           else:
              print(f"Parcel {i+1}: Rejected")

        print(f"Accepted pracels: {accepted_parcels}")
        print(f"Loaded weight: {van_capacity_int - remaining_capacity} kg")
        print(f"Remaining capacity: {remaining_capacity} kg")
        parcel_weights_list.clear() #"temporary" solution for running it multiple times without closing the program

     elif menychoice == "6":
        """Task 6"""

     elif menychoice == "7":
        """Task 7"""

     elif menychoice == "8":
        """Task 8"""
     else:
       print("Error - Select a service from 1 to 8.")
    pass


#task2: validate a booking reference
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
#task3: calculate a delivery quote
def calculate_quote(weight, distance, service_code):
    if weight <= 0 or distance <= 0:
        return "Weight and distance must be positive numbers."
    if service_code == "S" or service_code == "Standard":
        service_multiplier = 1.00
    elif service_code == "X" or service_code == "Express":
        service_multiplier = 1.25
    elif service_code == "P" or service_code == "Priority":
        service_multiplier = 1.60
    else:
        return "Invalid service code. Please choose 'S', 'X', or 'P' or 'Standard', 'Express', or 'Priority'."
    base_charge = 45.00
    weight_rate = 4.50 * weight
    distance_rate = 6.50 * distance

    delivery_quote = base_charge + weight_rate + distance_rate
    service_quote = delivery_quote * service_multiplier
    print(f"Distance(km): {distance}")
    print(f"Weight(kg): {weight}")
    print(f"Service code: {service_code}")
    print(f"Delivery quote: ${service_quote:.2f}")

    return service_quote
    
#task 4 consolidate parcel labels
def consolidate_labels(scanned_labels):
    raw_labels = scanned_labels.split(",")
    cleaned_labels = []
    for label in raw_labels:
        cleaned_label = label.strip().upper()
        if cleaned_label:
            cleaned_labels.append(cleaned_label)
    return cleaned_labels

def print_labels(cleaned_labels):
    print("Unique Parcel Labels:")
    count = 0
    for label in cleaned_labels:
        count += 1
        print(f"{count}. {label}")     
        print(f"Total unique parcels: {len(cleaned_labels)}")
