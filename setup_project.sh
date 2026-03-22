#!/bin/bash

# ============================================================
# 10Alytics Hackathon 2025 - Project Setup Script
# Run this from your terminal inside the project folder:
#   bash setup_project.sh
# ============================================================

PROJECT_DIR="/mnt/d/DS PROJECTS/10alytics_Hackathon"

echo "🚀 Setting up 10Alytics Hackathon project structure..."

# --- Create directories ---
mkdir -p "$PROJECT_DIR/data/raw"
mkdir -p "$PROJECT_DIR/data/processed"
mkdir -p "$PROJECT_DIR/notebooks"
mkdir -p "$PROJECT_DIR/src"
mkdir -p "$PROJECT_DIR/outputs/figures"
mkdir -p "$PROJECT_DIR/outputs/reports"
mkdir -p "$PROJECT_DIR/models"

echo "✅ Directories created."

# --- Move raw data ---
if [ -f "$PROJECT_DIR/10Alytics_Fiscal_Data.csv" ]; then
    mv "$PROJECT_DIR/10Alytics_Fiscal_Data.csv" "$PROJECT_DIR/data/raw/"
    echo "✅ Moved 10Alytics_Fiscal_Data.csv → data/raw/"
fi

if [ -f "$PROJECT_DIR/10Alytics_Fiscal_Panel_Data.csv" ]; then
    mv "$PROJECT_DIR/10Alytics_Fiscal_Panel_Data.csv" "$PROJECT_DIR/data/processed/"
    echo "✅ Moved 10Alytics_Fiscal_Panel_Data.csv → data/processed/"
fi

# --- Move existing notebook ---
if [ -f "$PROJECT_DIR/10AlyticsHack.ipynb" ]; then
    cp "$PROJECT_DIR/10AlyticsHack.ipynb" "$PROJECT_DIR/notebooks/10AlyticsHack_original_backup.ipynb"
    mv "$PROJECT_DIR/10AlyticsHack.ipynb" "$PROJECT_DIR/notebooks/01_02_03_data_eda_anomaly.ipynb"
    echo "✅ Moved notebook → notebooks/ (backup copy kept)"
fi

# --- Move existing figures ---
if [ -f "$PROJECT_DIR/correlation_heatmap.png" ]; then
    mv "$PROJECT_DIR/correlation_heatmap.png" "$PROJECT_DIR/outputs/figures/"
    echo "✅ Moved correlation_heatmap.png → outputs/figures/"
fi

# --- Create src/__init__.py ---
touch "$PROJECT_DIR/src/__init__.py"

# --- Create .gitignore ---
cat > "$PROJECT_DIR/.gitignore" << 'EOF'
# Python
__pycache__/
*.py[cod]
*.pyo
.env
.venv
env/
venv/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Data (optional: comment out if you want to track data)
# data/raw/
# data/processed/

# Models (large files)
models/*.pkl
models/*.joblib

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
EOF

echo "✅ .gitignore created."
echo ""
echo "🎉 Project structure ready! Here's your layout:"
echo ""
find "$PROJECT_DIR" -not -path '*/\.*' | sed 's|[^/]*/|  |g'
