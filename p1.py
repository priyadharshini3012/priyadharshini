import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize session state if not already initialized
if 'patients_data' not in st.session_state:
    st.session_state.patients_data = pd.DataFrame({
        'Patient ID': [1, 2, 3],
        'Name': ['John Doe', 'Jane Smith', 'Samuel Johnson'],
        'Age': [45, 38, 28],
        'Gender': ['Male', 'Female', 'Male'],
        'Contact': ['1234567890', '9876543210', '4567891230'],
        'Medical History': ['Hypertension', 'Asthma', 'Back Pain']
    })

if 'doctors_data' not in st.session_state:
    st.session_state.doctors_data = pd.DataFrame({
        'Doctor ID': [101, 102, 103],
        'Name': ['Dr. Alice', 'Dr. Bob', 'Dr. Charlie'],
        'Specialization': ['Cardiology', 'Neurology', 'Orthopedics'],
        'Experience (Years)': [10, 15, 8]
    })

if 'appointments_data' not in st.session_state:
    st.session_state.appointments_data = pd.DataFrame({
        'Appointment ID': [1, 2],
        'Patient Name': ['John Doe', 'Jane Smith'],
        'Doctor Name': ['Dr. Alice', 'Dr. Bob'],
        'Appointment Date': ['2025-02-01', '2025-02-02'],
        'Appointment Time': ['10:00 AM', '02:00 PM'],
        'Status': ['Scheduled', 'Scheduled']
    })

# Function to display data visualizations
def display_visualizations():
    st.subheader("Hospital Overview Visualizations")

    # Gender Distribution Pie Chart
    gender_dist = st.session_state.patients_data['Gender'].value_counts()
    st.write("Gender Distribution of Patients")
    fig, ax = plt.subplots()
    ax.pie(gender_dist, labels=gender_dist.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set2", n_colors=len(gender_dist)))
    ax.axis('equal')
    st.pyplot(fig)

    # Appointment Status Pie Chart
    status_dist = st.session_state.appointments_data['Status'].value_counts()
    st.write("Appointment Status Distribution")
    fig, ax = plt.subplots()
    ax.pie(status_dist, labels=status_dist.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("coolwarm", n_colors=len(status_dist)))
    ax.axis('equal')
    st.pyplot(fig)

    # Doctor Specialization Bar Chart
    doctor_specialization = st.session_state.doctors_data.groupby('Specialization').size()
    st.write("Number of Doctors by Specialization")
    fig, ax = plt.subplots()
    doctor_specialization.plot(kind='bar', ax=ax, color=sns.color_palette("Paired", n_colors=len(doctor_specialization)))
    ax.set_title("Doctors by Specialization")
    st.pyplot(fig)

# Function for Recent Activity Feed
def display_recent_activity():
    st.subheader("Recent Activity Feed")
    # Simulate recent activity feed
    activity_data = [
        "Added new patient: John Doe",
        "Appointment booked for Jane Smith with Dr. Bob",
        "Added new doctor: Dr. Alice",
        "Appointment rescheduled for Samuel Johnson",
        "Added new patient: Lisa Brown",
    ]
    
    for activity in activity_data:
        st.markdown(f"- {activity}")

# Main Streamlit interface
def main():
    st.title("Creative Hospital Management System")

    menu = ["Home", "Dashboard", "Patients", "Doctors", "Appointments", "Search", "Export Data"]
    choice = st.sidebar.selectbox("Select a Section", menu)

    if choice == "Home":
        st.subheader("Welcome to the Creative Hospital Management System!")
        st.write("Manage your patients, doctors, and appointments easily.")
        
        # Front Page with Quick Actions and Visualizations
        st.write("### Quick Actions")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Add Patient"):
                st.session_state['patients_data'] = pd.concat([st.session_state['patients_data'], pd.DataFrame([{
                    'Patient ID': len(st.session_state.patients_data) + 1,
                    'Name': 'New Patient',
                    'Age': 30,
                    'Gender': 'Male',
                    'Contact': '0000000000',
                    'Medical History': 'None'
                }])], ignore_index=True)
                st.success("Patient Added!")

        with col2:
            if st.button("Add Doctor"):
                st.session_state['doctors_data'] = pd.concat([st.session_state['doctors_data'], pd.DataFrame([{
                    'Doctor ID': len(st.session_state.doctors_data) + 1,
                    'Name': 'New Doctor',
                    'Specialization': 'General',
                    'Experience (Years)': 5
                }])], ignore_index=True)
                st.success("Doctor Added!")
        
        # Display Visualizations
        display_visualizations()
        display_recent_activity()

    elif choice == "Dashboard":
        # Show key statistics and analytics
        total_patients = len(st.session_state.patients_data)
        total_doctors = len(st.session_state.doctors_data)
        total_appointments = len(st.session_state.appointments_data)

        st.subheader("Dashboard")
        st.write(f"Total Patients: {total_patients}")
        st.write(f"Total Doctors: {total_doctors}")
        st.write(f"Total Appointments: {total_appointments}")
        display_visualizations()

    elif choice == "Patients":
        st.subheader("Patient Information")
        patient_option = st.selectbox("Select an Action", ["View All Patients", "Add New Patient", "Search Patient"])

        if patient_option == "View All Patients":
            st.write(st.session_state.patients_data)
        elif patient_option == "Add New Patient":
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=1, max_value=120)
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            contact = st.text_input("Contact Number")
            medical_history = st.text_area("Medical History")

            if st.button("Add Patient"):
                new_patient = {
                    'Patient ID': len(st.session_state.patients_data) + 1,
                    'Name': name,
                    'Age': age,
                    'Gender': gender,
                    'Contact': contact,
                    'Medical History': medical_history
                }
                st.session_state.patients_data = pd.concat([st.session_state.patients_data, pd.DataFrame([new_patient])], ignore_index=True)
                st.success("Patient added successfully!")

        elif patient_option == "Search Patient":
            search_name = st.text_input("Enter Patient Name to Search:")
            if search_name:
                patient = st.session_state.patients_data[st.session_state.patients_data['Name'].str.contains(search_name, case=False)]
                if not patient.empty:
                    st.write(patient)
                else:
                    st.warning("No matching patient found!")

    elif choice == "Doctors":
        st.subheader("Doctor Information")
        doctor_option = st.selectbox("Select an Action", ["View All Doctors", "Add New Doctor", "Search Doctor"])

        if doctor_option == "View All Doctors":
            st.write(st.session_state.doctors_data)
        elif doctor_option == "Add New Doctor":
            name = st.text_input("Name")
            specialization = st.text_input("Specialization")
            experience = st.number_input("Experience (Years)", min_value=0)

            if st.button("Add Doctor"):
                new_doctor = {
                    'Doctor ID': len(st.session_state.doctors_data) + 1,
                    'Name': name,
                    'Specialization': specialization,
                    'Experience (Years)': experience
                }
                st.session_state.doctors_data = pd.concat([st.session_state.doctors_data, pd.DataFrame([new_doctor])], ignore_index=True)
                st.success("Doctor added successfully!")

        elif doctor_option == "Search Doctor":
            search_name = st.text_input("Enter Doctor Name to Search:")
            if search_name:
                doctor = st.session_state.doctors_data[st.session_state.doctors_data['Name'].str.contains(search_name, case=False)]
                if not doctor.empty:
                    st.write(doctor)
                else:
                    st.warning("No matching doctor found!")

    elif choice == "Appointments":
        st.subheader("Appointment Management")
        appointment_option = st.selectbox("Select an Action", ["View All Appointments", "Book Appointment"])

        if appointment_option == "View All Appointments":
            st.write(st.session_state.appointments_data)
        elif appointment_option == "Book Appointment":
            patient_name = st.selectbox("Select Patient", st.session_state.patients_data['Name'])
            doctor_name = st.selectbox("Select Doctor", st.session_state.doctors_data['Name'])
            appointment_date = st.date_input("Select Appointment Date")
            appointment_time = st.selectbox("Select Time Slot", ["9:00 AM", "10:00 AM", "11:00 AM", "1:00 PM", "2:00 PM", "3:00 PM"])

            if st.button("Book Appointment"):
                new_appointment = {
                    'Appointment ID': len(st.session_state.appointments_data) + 1,
                    'Patient Name': patient_name,
                    'Doctor Name': doctor_name,
                    'Appointment Date': str(appointment_date),
                    'Appointment Time': appointment_time,
                    'Status': 'Scheduled'
                }
                st.session_state.appointments_data = pd.concat([st.session_state.appointments_data, pd.DataFrame([new_appointment])], ignore_index=True)
                st.success("Appointment booked successfully!")

    elif choice == "Export Data":
        export_option = st.selectbox("Select Data to Export", ["Patients", "Doctors", "Appointments"])
        
        if export_option == "Patients":
            st.download_button(
                label="Download Patients Data as CSV",
                data=st.session_state.patients_data.to_csv(index=False),
                file_name="patients_data.csv",
                mime="text/csv"
            )
        
        elif export_option == "Doctors":
            st.download_button(
                label="Download Doctors Data as CSV",
                data=st.session_state.doctors_data.to_csv(index=False),
                file_name="doctors_data.csv",
                mime="text/csv"
            )

        elif export_option == "Appointments":
            st.download_button(
                label="Download Appointments Data as CSV",
                data=st.session_state.appointments_data.to_csv(index=False),
                file_name="appointments_data.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()
