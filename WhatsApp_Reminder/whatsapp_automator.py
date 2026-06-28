import pandas as pd
import pywhatkit as kit
import time

# ==========================================
# STEP 1: READ CLIENT DATA FROM EXCEL
# ==========================================
df = pd.read_excel("due_payments.xlsx")

print("🚀 Starting WhatsApp Automation Script...")
print("⚠️ Note: Make sure you are logged into WhatsApp Web on your default browser!")

# ==========================================
# STEP 2: LOOP THROUGH AND SEND REMINDERS
# ==========================================
for index, row in df.iterrows():
    name = row['Customer Name']
    phone = f"+{str(row['Phone Number'])}" # Formats number with '+' sign
    amount = row['Pending Amount']
    
    # Create a personalized message
    message = f"Hello {name}, this is a friendly reminder that your payment of {amount} is pending. Kindly clear it at your earliest convenience. Thank you!"
    
    print(f"\n⏳ Preparing message for {name} ({phone})...")
    
    try:
        # sendwhatmsg_instantly opens WhatsApp web and sends the message immediately
        # wait_time=15 gives your browser 15 seconds to load up before hitting send
        kit.sendwhatmsg_instantly(phone_no=phone, message=message, wait_time=15, tab_close=True)
        print(f"✅ Success: Reminder sent to {name}!")
        
        # Give the system 10 seconds to rest and close tabs before starting the next message
        time.sleep(10)
        
    except Exception as e:
        print(f"❌ Failed to send to {name}: {e}")

print("\n⚡ All scheduled reminders processed!")