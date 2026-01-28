import React from 'react';
import { FaNewspaper, FaSearch, FaUserCircle } from 'react-icons/fa';
import { HiMenuAlt3 } from 'react-icons/hi';

function Header() {
  return (
    <header className="flex items-center justify-between px-6 py-4 bg-white border-b border-gray-100 sticky top-0 z-50">
      
      {/* Brand Section */}
      <div className="flex items-center gap-2">
        <div className="bg-blue-600 p-1.5 rounded-lg">
          <FaNewspaper className="text-white text-xl" />
        </div>
        <span className="text-xl font-bold tracking-tight text-gray-800">
          NewsAgent
        </span>
      </div>

      {/* Action Icons Section */}
      <div className="flex items-center gap-5 text-gray-500">
        <button className="hover:text-blue-600 transition-colors">
          <FaSearch size={18} />
        </button>
        <button className="hover:text-blue-600 transition-colors">
          <FaUserCircle size={22} />
        </button>
        <button className="md:hidden hover:text-blue-600 transition-colors">
          <HiMenuAlt3 size={24} />
        </button>
      </div>

    </header>
  );
}

export default Header;