'use client';

import { useEffect, useState } from 'react';

// First, define an interface for your data structure
interface ScrapeData {
  korean_title: string;
  image: string;
  // add other properties as needed
}

export default function Home() {
  const [data, setData] = useState<ScrapeData | null>(null);
  let imageUrl = "https://thumbnews.nateimg.co.kr/view610///news.nateimg.co.kr/orgImg/tv/2025/01/27/1740734.jpg";
  
  // Extract the original image URL
  imageUrl = imageUrl.split('///').pop() || imageUrl;
  imageUrl = 'https://' + imageUrl;
  

  console.log('Processing URL:', imageUrl); // Let's see what URL we're trying to load

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
      <img 
        id="mainimg0"
        src={imageUrl} 
        alt="Scraped main image"
      />
    </main>
  );
}