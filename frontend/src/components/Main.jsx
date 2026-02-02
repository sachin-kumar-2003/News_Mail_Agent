import React, { useState } from 'react';
import { FaInfoCircle, FaCheckCircle, FaPlusCircle, FaEnvelope, FaSearch } from 'react-icons/fa';
import { IoSend } from 'react-icons/io5';
import axios from "axios"

function Main() {
  const serverUrl = import.meta.env.VITE_SERVER_URL;
  // const serverUrl = "http://127.0.0.1:8000"
  const [usermail, setMail] = useState("")
  const [userquery, setQuery] = useState("")

  const handleSubmit = async () => {
    console.log("api calling...")
    console.log("user mail is ", usermail)
    console.log("user query is ", userquery)
    if(usermail == "" || userquery == ""){
      alert("check your mail or query")
      return;
    }

    await axios.post(`${serverUrl}/news`, {
      usermail: usermail,
      userquery: userquery
    }).then((response) =>{
      alert(`${response.data.response}`)
    }).catch((err) =>{
      console.log("something is wrong in backend" + err.message)
    })
    
  }


  return (
    <main className="max-w-4xl mx-auto p-6">
      <div className="flex flex-col md:flex-row gap-8 items-start bg-white rounded-2xl p-8 shadow-sm border border-gray-100">

        {/* Left/Top Section: Info List */}
        <div className="flex-1 space-y-4">
          <div className="space-y-3">
            <ul className="space-y-4">
              <li className="flex items-center gap-3 text-gray-700 font-medium">
                <FaInfoCircle className="text-blue-500 shrink-0" />
                <span>this is news agent</span>
              </li>
              <li className="flex items-center gap-3 text-gray-600">
                <FaCheckCircle className="text-green-500 shrink-0" />
                <span>right now only above news functionality is added</span>
              </li>
              <li className="flex items-center gap-3 text-gray-500 italic">
                <FaPlusCircle className="text-purple-500 shrink-0" />
                <span>sooner we will add more thing which is liked by users.</span>
              </li>
            </ul>
          </div>
        </div>
        {/* Right/Bottom Section: Actions */}
        <div className="w-full md:w-auto space-y-6">

          {/* Email Input Group */}
          <div className="relative group">
            <FaEnvelope className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-blue-500 transition-colors" />
            <input
              type="email"
              placeholder="Enter your email..."
              className="w-full md:w-[300px] pl-10 pr-4 py-2.5 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all"
              onChange={(e) => { setMail(e.target.value) }}
            />
          </div>
          {/* Query & Button Group */}
          <div className="space-y-3 p-4 bg-blue-50 rounded-xl border border-blue-100">
            <div className="relative group">
              <FaSearch className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 group-focus-within:text-blue-500" />
              <input
                type="text"
                placeholder='what the latest sports news'
                className="w-full pl-10 pr-4 py-2.5 bg-white border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500/20 transition-all"
                onChange={(e) => { setQuery(e.target.value) }}
              />
            </div>
            <button className="w-full flex items-center justify-center gap-2 px-6 py-2.5 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 transition-colors shadow-lg shadow-blue-200" onClick={()=>{handleSubmit()}}>
              <span>Send mail</span>
              <IoSend />
            </button>
          </div>
        </div>

      </div>
    </main>
  );
}

export default Main;