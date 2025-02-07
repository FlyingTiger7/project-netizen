'use client';

import { useEffect, useState } from 'react';

// First, define an interface for your data structure
interface ScrapeData {
  korean_title: string;
  // add other properties as needed
}

export default function Home() {
  const [data, setData] = useState<ScrapeData | null>(null);

  useEffect(() => {
    fetch('/api/scrape')
      .then(res => res.json())
      .then((data: ScrapeData) => setData(data))
      .catch(err => console.error('Error:', err));
  }, []);

  return (
    <main>
      <h1>Scraper Results</h1>
      <div>{data?.korean_title}</div>
    </main>
  );
}