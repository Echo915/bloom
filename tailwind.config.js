/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/base.html",
    "./templates/sections.html",
  ],
  theme: {
    // colors: {
    //   "primary": "#0069D9",
    //   "secondary": "#F7F7F7",
    // },    
    extend: {
      btn: [
        "rounded-md",
        "shadow", 
        "px-3", 
        "py-2", 
        "text-white", 
        "bg-blue-400",
      ]
    },
  },
  plugins: [],
}
