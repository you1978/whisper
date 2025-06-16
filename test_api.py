#!/usr/bin/env python3
"""Test the Whisper API endpoints"""

import requests
import sys

API_URL = "https://whisper-production-130b.up.railway.app"

def test_health():
    """Test health endpoint"""
    print("Testing health endpoint...")
    response = requests.get(f"{API_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200

def test_root():
    """Test root endpoint"""
    print("\nTesting root endpoint...")
    response = requests.get(f"{API_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200

def test_transcribe_simple():
    """Test transcribe with a simple audio file"""
    print("\nTesting transcribe endpoint with sample audio...")
    
    # Create a simple test by sending the audio file
    with open("sample/Audio 2_002_1S7X0H.L.wav", "rb") as f:
        files = {"audio": f}
        data = {
            "language": "ja",
            "task": "transcribe"
        }
        
        print("Sending request (this may take a while)...")
        try:
            response = requests.post(
                f"{API_URL}/transcribe", 
                files=files, 
                data=data,
                timeout=300  # 5 minutes timeout
            )
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                print(f"Transcribed text: {result.get('text', 'No text returned')}")
                print(f"Detected language: {result.get('language', 'Unknown')}")
            else:
                print(f"Error: {response.text}")
            return response.status_code == 200
        except requests.exceptions.Timeout:
            print("Request timed out after 5 minutes")
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False

if __name__ == "__main__":
    print(f"Testing Whisper API at {API_URL}\n")
    
    # Run tests
    tests = [
        ("Health Check", test_health),
        ("Root Endpoint", test_root),
        ("Transcribe Audio", test_transcribe_simple)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            passed = test_func()
            results.append((name, passed))
        except Exception as e:
            print(f"Error in {name}: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    for name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{name}: {status}")
    
    # Exit with appropriate code
    all_passed = all(passed for _, passed in results)
    sys.exit(0 if all_passed else 1)