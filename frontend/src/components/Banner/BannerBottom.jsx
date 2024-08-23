import React from 'react'
import {
    FaHeadphones,
    FaWallet,
    FaCheckCircle,
} from "react-icons/fa";
import { IoSpeedometer } from "react-icons/io5";

const ServiceData = [
  {
      id: 1,
      icon: <IoSpeedometer className='text-4xl sm:text-5xl text-brandBlue'/>,
      title: "Fast Shipping",
      description: "The Fastest Shipping Available To You "
  },
  {
      id: 2,
      icon: <FaHeadphones className='text-4xl sm:text-5xl text-brandBlue'/>,
      title: "2/47 Customer Support",
      description: "Online Support, Just One Call Away"
  },
  {
      id: 3,
  FaWallet,
  icon: <FaWallet className='text-4xl sm:text-5xl text-brandBlue'/>,
      title: "Budget Friendly",
      description: "Get Items Of Your Choice At Affordable Or Discounted "
  },
  {
      id: 4,
      icon: <FaCheckCircle className='text-4xl sm:text-5xl text-brandBlue'/>,
      title: "Secure Payments",
      description: "You Also Get money Back After 30days"
  },
]

const BannerBottom = () => {
  return (
    <div>
    <div className="container py-20 md:my-20">
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-12 gap-y-8">
            {ServiceData.map((data) =>(
            <div className='flex flex-col items-start sm:flex-row gap-4' key={data.id}>
                {data.icon}
                <div>
                    <h1 className='lg:text-xl font-bold text-gray-900'>{data.title}</h1>
                    <h1 className='text-gray-400 text-sm'>{data.description}</h1>
                </div>
            </div>
            ))}
        </div>
    </div>
</div>
  );
};

export default BannerBottom;
