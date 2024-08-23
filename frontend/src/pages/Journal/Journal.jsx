import React, { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import Breadcrumbs from "../../components/pageProps/Breadcrumbs";

const Journal = () => {
  const location = useLocation();
  const [prevLocation, setPrevLocation] = useState("");
  useEffect(() => {
    setPrevLocation(location.state.data);
  }, [location]);
  return ( 
    <div className="max-w-container mx-auto px-4">
      <Breadcrumbs title="Novo Swap" prevLocation={prevLocation} />
      <div className="pb-10">
        <h1 className="max-w-[600px] text-base text-lightText mb-2">
          <span className="text-brandGreen font-semibold text-lg">Novo-Swap</span>{" "}
          is a new feature that allows users to Swap existing valuable products for Upgrades
        </h1>
        <Link to="/shop">
          <button className="w-52 h-10 bg-brandBlue text-white hover:bg-brandGreen duration-300">
            Continue Shopping
          </button>
        </Link>
      </div>
    </div>
  );
};

export default Journal;
