import React, { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import Breadcrumbs from "../../components/pageProps/Breadcrumbs";

const About = () => {
  const location = useLocation();
  const [prevLocation, setPrevLocation] = useState("");
  useEffect(() => {
    setPrevLocation(location.state.data);
  }, [location]);
  return (
    <div className="max-w-container mx-auto px-4">
      <Breadcrumbs title="About" prevLocation={prevLocation} />
      <div className="pb-10">
        <h1 className="max-w-[600px] text-base text-lightText mb-2">
          <span className="text-primeColor font-semibold text-lg">
            Novo Mall
          </span>{" "}<br/>
          Welcome! At Novo-Mall, we’re more
          than just an eCommerce store—we’re a community passionate about Technology.
           Our mission is simple: to provide you with
          high-quality products and services that enhance your life and bring you
          joy. Who We Are Founded in [Year], our journey began with a vision to
          revolutionize [industry/niche]. Our team of dedicated professionals
          combines [mention experience, skills, or unique qualities] to curate
          an exceptional selection of [products/services]. We pride ourselves on
          our commitment to quality, innovation, and customer satisfaction. Our
          Values Customer-Centric: Your needs are our top priority. We’re here
          to listen, assist, and ensure that your shopping experience is
          seamless and enjoyable. Quality: We meticulously select every item to
          meet our high standards. Our goal is to offer you only the best.
          Integrity: Honesty and transparency are at the core of our operations.
          We strive to build trust through every interaction. Innovation: We
          embrace change and continuously seek new ways to improve our offerings
          and services. What We Offer Explore our diverse range of
          [products/services], designed to cater to every taste and preference.
          From [specific product types] to [other categories], we’re here to
          meet your needs with unparalleled quality and service. Our Promise At
          [Your Company Name], we’re committed to providing an exceptional
          shopping experience. Whether you're browsing from the comfort of your
          home or seeking expert advice, our team is here to assist you every
          step of the way. Thank you for choosing [Your Company Name]. We look
          forward to serving you and becoming a part of your [industry/niche]
          journey. Stay Connected Follow us on [social media links] for the
          latest updates, promotions, and more. Have questions? Feel free to
          reach out to our customer service team at [contact information]. We're
          always here to help! Welcome to the [Your Company Name] family!
          Sincerely, The [Your Company Name] Team
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
 
export default About;
