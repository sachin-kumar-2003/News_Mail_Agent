import React from 'react';
import { BiGlobe, BiFlag, BiTrophy, BiBriefcaseAlt2 } from 'react-icons/bi';
import { IoSend } from 'react-icons/io5';

function Body() {
  const categories = [
    { name: 'International News', icon: <BiGlobe /> },
    { name: 'National News', icon: <BiFlag /> },
    { name: 'Sports News', icon: <BiTrophy /> },
    { name: 'Business News', icon: <BiBriefcaseAlt2 /> },
  ];

  return (
    <div className="flex flex-col md:flex-row items-center justify-between gap-6 px-6 py-8 bg-gray-50 border-b border-gray-200">
      
      {/* Section 1: Categories */}
      <div className="flex flex-wrap items-center gap-3">
        {categories.map((cat, index) => (
          <button
            key={index}
            className="flex items-center gap-2 px-4 py-2 bg-white border border-gray-200 rounded-full text-sm font-medium text-gray-700 hover:border-blue-500 hover:text-blue-600 transition-all shadow-sm"
          >
            <span className="text-lg">{cat.icon}</span>
            {cat.name}
          </button>
        ))}
      </div>
    </div>
  );
}

export default Body;