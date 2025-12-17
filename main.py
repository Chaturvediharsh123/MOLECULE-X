"""
Main entry point for the Molecule-X system.
"""
import subprocess
import sys
import os

def main():
    print("Molecule-X: AI-Native Multi-Agent Drug Repurposing System")
    print("=" * 60)
    print("Choose an option:")
    print("1. Launch Drug Repurposing Assistant (Web UI)")
    print("2. Train Toxicity Prediction Model")
    print("3. Run Simulation Impact Analysis")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice == "1":
        print("Launching Drug Repurposing Assistant...")
        # Change to src directory and run streamlit
        try:
            subprocess.run([sys.executable, "-m", "streamlit", "run", "src/app.py"], check=True)
        except subprocess.CalledProcessError:
            print("Error launching Streamlit. Make sure you have Streamlit installed.")
            print("Install it with: pip install streamlit")
    
    elif choice == "2":
        print("Training toxicity prediction model...")
        try:
            # Run the training script
            subprocess.run([sys.executable, "src/train.py"], check=True)
        except subprocess.CalledProcessError:
            print("Error during model training.")
    
    elif choice == "3":
        print("Running simulation impact analysis...")
        try:
            # Run the simulation script
            subprocess.run([sys.executable, "src/simulate_impact.py"], check=True)
        except subprocess.CalledProcessError:
            print("Error during simulation analysis.")
    
    elif choice == "4":
        print("Exiting Molecule-X. Goodbye!")
        sys.exit(0)
    
    else:
        print("Invalid choice. Please run the program again and select a valid option.")
        sys.exit(1)

if __name__ == "__main__":
    main()