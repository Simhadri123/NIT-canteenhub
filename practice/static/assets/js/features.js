

// --- Cart Modal ---
const cartOverlay = document.querySelector('.cart-overlay');
const cartInnerlay = document.querySelector('.cart-innerlay');
const cartBtn = document.querySelectorAll('#cart-btn');


// Cart Button
cartBtn.forEach(element => {
    element.addEventListener('click', () => {
        cartOverlay.classList.add('show');
        cartInnerlay.classList.add('showCart');
    });
})



// Home/Vision Footer
var customerFooter = document.querySelectorAll('.customer-footer');
function customerFooterUI() {
    if (customerFooter){
        customerFooter.forEach(element => {
            element.innerHTML = `
            <section class="container-min">
            <!-- Upper Footer -->
                <main class="grid grid-3">
                    <!-- About College -->
                    <article class="about">
                        <h1 class="sm">about</h1>
                        <p> National Institute of Technology Andhra Pradesh is governed by Central Government
                        was founded in 2019 & it is running succesfully It is located in tadepalliguem.</p>
                        <ul class="py-1">
                            <li><i class="fab fa-facebook-f"></i><a href="https://www.facebook.com/" target="_blank"> Facebook</a></li>
                            <li><i class="fab fa-instagram"></i><a href="https://www.instagram.com/malwa_institute_of_technology/" target="_blank">Instagram</a></li>
                        </ul>
                    </article>
                    <!-- Navigation Links -->
                    <article class="quick-links">
                        <ul>
                            <h1 class="sm">Quick Links</h1>
                            <li><a href=" https://www.nitandhra.ac.in/main/" target="_blank">NIT AP </a></li>
                        </ul>

                    
                    </article>
                    <!-- Contact Details -->
                    <article class="contact">
                        <ul>
                            <h1 class="sm">Contact Information</h1>
                            <li> <i class="fas fa-phone-alt"></i>0123456789 <p></p></li>
                            <li> <i class="fas fa-envelope"></i> <p>admission@nitandhrapradesh.ac.in</p></li>
                            <li> <i class="fas fa-map-marker-alt"></i> <p>TADEPALLIGUDEM BYPASS ROAD,WEST GODAVARI,534101</p></li>
                            <li> <i class="fas fa-globe-asia"></i> <p>For Professional Courses, Visit: www.nitandhrapradesh.in</p></li>
                        </ul>
                    </article>
                </main>
                <!-- SKV Info -->
                <main class="deep-devs flex">
                    <div>© Copyright 2024 - 2025. All Rights Reserved</div>
                </main>
            </section>
        `;
        })
    }
}
customerFooterUI()

// Authenticated User Footer
var userFooter = document.querySelectorAll('#user-footer');
function userFooterUI() {
    if (userFooter){
        userFooter.forEach(element => {
            element.innerHTML = `
            <section class="container-min">
            <!-- Upper Footer -->
                <main class="grid grid-3">
                    <!-- About College -->
                    <article class="about">
                        <h1 class="sm">about</h1>
                        <p>National Institute of Technology Andhra Pradesh is governed by Central Government
                        was founded in 2019 & it is running succesfully It is located in tadepalliguem.</p>
                        <ul class="py-1">
                            <li><i class="fab fa-facebook-f"></i><a href="https://www.facebook.com/" target="_blank"> Facebook</a></li>
                            <li><i class="fab fa-instagram"></i><a href="https://www.instagram.com/" target="_blank">Instagram</a></li>
                        </ul>
                    </article>
                    <!-- Navigation Links -->
                    <article class="quick-links">
                        <ul>
                            <h1 class="sm">Quick Links</h1>
                            <li><a href=" https://www.nitandhra.ac.in/main/" target="_blank">NIT AP
                            </a></li>
                        </ul>
                    </article>
                    <!-- Contact Details -->
                    <article class="contact">
                        <ul>
                            <h1 class="sm">Contact Information</h1>
                            <li> <i class="fas fa-phone-alt"></i> <p>0123456789</p></li>
                            <li> <i class="fas fa-envelope"></i> <p>admission@nitandhrapradesh.ac.in</p></li>
                            <li> <i class="fas fa-map-marker-alt"></i> <p>TADEPALLIGUDEM BYPASS ROAD,WEST GODAVARI,534101</p></li>
                            <li> <i class="fas fa-globe-asia"></i> <p>Visit:https://www.nitandhra.ac.in/main/</p></li>
                        </ul>
                    </article>
                </main>
                <!-- SKV Info -->
                <main class="deep-devs flex">
                    <div>© Copyright 2024 - 2025. All Rights Reserved</div>
                </main>
            </section>
        `;
        })
    }
}
userFooterUI()


