#!/bin/bash

cd backend
rm -rf venv

cd ../frontend
rm -rf frontend/node_modules
rm -rf frontend/build
rm frontend/package-lock.json