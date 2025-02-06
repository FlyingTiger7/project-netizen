import { NextResponse } from 'next/server';
import { spawn } from 'child_process';

export async function GET() {
  const pythonProcess = spawn('python3', ['app/scraper.py']);
  
  return new Promise((resolve) => {
    let dataString = '';

    // Collect all data
    pythonProcess.stdout.on('data', (data) => {
      console.log('Raw Python output:', data.toString());  // Log raw output
      dataString += data.toString();
    });

    // Add error handling
    pythonProcess.stderr.on('data', (data) => {
      console.error('Python error:', data.toString());
    });

    // When Python is done
    pythonProcess.on('close', (code) => {
      console.log('Final collected data:', dataString);  // Log final string
      console.log('Exit code:', code);

      try {
        // Parse the collected JSON data
        const jsonData = JSON.parse(dataString);
        console.log('Parsed JSON:', jsonData);  // Log parsed JSON
        resolve(NextResponse.json(jsonData));
      } catch (error: any) {  // Type the error as any for now
        console.error('Parse error:', error.message);  // Log parse error
        resolve(NextResponse.json({ 
          text: 'Error parsing data',
          raw: dataString,  // Include raw data in response
          error: error instanceof Error ? error.message : 'Unknown error'
        }));
      }
    });
  });
}