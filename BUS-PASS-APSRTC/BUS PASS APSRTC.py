import qrcode
import json

def generate_qr(bus_pass_details, filename="bus_pass_qr.png"):
    data_json = json.dumps(bus_pass_details)  # Convert dictionary to JSON string
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data_json)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"Bus pass QR code saved as {filename}")

if __name__ == "__main__":
    bus_pass_details = {
        "MR_NO": "MR12671067",
        "ID": "12439649<>7?0116971",
        "Name": "CH SANDEEP",
        "Age": "20",
        "Aadhar": "248394481777",
        "Institution": "PRAGATI",
        "Route_Details": "KAKINADA TO RAMESAMPETA",
        "No_of_Passes_in_Day": "2",
        "Pass_Valid_Upto": "ONE MONTH"
    }
    generate_qr(bus_pass_details)
