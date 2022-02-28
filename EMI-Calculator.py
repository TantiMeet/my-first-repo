# Write the code for creating the EMI calculator app
import streamlit as st

def calculate_emi(p,n,r):
  emi = p * (r / 100) * (((1 + (r / 100)) ** n) / (((1 + (r / 100)) ** n) -1))
  st.write(f"Your EMI is {emi:.3f}.")
  return round(emi,3)
  
st.title("EMI calculator")
principal = st.slider("principal", 10000, 100000)
tenure = st.slider("tenure", 1, 25)
roi = st.slider("rate of interest", 1.00, 20.00)
if st.button("calculate"):
  calculated_emi = calculate_emi(principal, tenure*12, roi/12)
  st.write("If the Principal Amount borrowed is ", principal,"for the tenure of ", tenure, "months with Rate od interest as ", roi, "percent per annum then the EMI will be ", calculated_emi)


# Write the code for creating the Improvised EMI calculator app

def calculate_emi(p, n, r,m):
  emi = p * (r / 100) * (((1 + (r / 100)) ** n) / (((1 + (r / 100)) ** n) -1))
  return round(emi, 3)

def calculate_outstanding_emi(p, n, r, m):
  out_emi = (p * ((1+(r/100))**n - (1+(r/100))**m)) / ((1+(r/100))**n - 1)
  return round(out_emi, 3)

st.title("Improvised EMI calculator app")

principal = st.slider("Principal", 10000, 100000)
tenure = st.slider("Tenure", 1, 25)
roi = st.slider("Rate of interest", 1.00, 20.00)
m = st.slider("Period after which the Outstanding Loan Balance is calculated(in months)", 1, (tenure * 12))

n = tenure * 12
r = roi / 12

if st.button("Calcualte EMI"):
  calculated_emi = calculate_emi(principal, n, r)
  st.write("If the Principal Amount borrowed is ", principal, "for the tenure of ", n, "months with Rate of interest as ", r, "percent per annum then the EMI will be ", calculated_emi)
if st.button("Calculate Outstanding Loan Balance"):
  loan = calculate_outstanding_emi(principal, n, r, m)
  st.write("Outstanding Balance Amount is ", loan)  