'use client';

import { useEffect, useState } from 'react';

export default function Home() {
  const [data, setData] = useState<string>("");

  useEffect(() => {
    fetch('/api/scrape')
      .then(res => res.json())
      .then(data => setData(data.korean_title))
      .catch(err => console.error('Error:', err));
  }, []);

  return (
    <main>
      <h1>Scraper Results</h1>
      <div>{data}</div>
    </main>
  );
}