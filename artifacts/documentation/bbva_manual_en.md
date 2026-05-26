# BBVA Mobile Application & Digital Banking: Master UI Guide

---

## Section 1: Onboarding, Authentication & Login Screen (Page 1)

### 1.1 Visual Layout & Topology

The initial screen of the BBVA Mobile Application serves as the primary gateway for both existing clients and new users. 

```
┌────────────────────────────────────────────────────────┐
│ BBVA                                                 ≡ │
├────────────────────────────────────────────────────────┤
│                                                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │ NIF, NIE, Tarjeta o Pasaporte                    │  │
│  └──────────────────────────────────────────────────┘  │
│                                                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Clave de acceso                                  │  │
│  └──────────────────────────────────────────────────┘  │
│                                                        │
│             ¿Has olvidado tu clave de acceso?          │
│                                                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │                  Iniciar sesión                  │  │
│  └──────────────────────────────────────────────────┘  │
│                                                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │               Crear clave de acceso              │  │
│  └──────────────────────────────────────────────────┘  │
│                                                        │
│                      Hazte cliente                     │
│                                                        │
└────────────────────────────────────────────────────────┘
```

*   **Top Header Area**:
    *   **BBVA Logo**: Positioned at the top center of the screen.
    *   **Lateral Menu Button `[≡]`**: Located at the top right corner. Tapping this button opens the sidebar menu containing configuration, security, and utility options.
*   **Central Input Wrapper**:
    *   **Username Input Field `[NIF, NIE, Tarjeta o Pasaporte]`**: Located in the upper-middle section of the screen. This field accepts alphanumeric characters representing the user's identity document.
    *   **Password Input Field `[Clave de acceso]`**: Positioned directly below the username field. This field masks characters for security.
    *   **Recovery Link `[¿Has olvidado tu clave de acceso?]`**: Centered directly below the password input field.
*   **Action Button Group**:
    *   **Primary Action Button `[Iniciar sesión]`**: A prominent button located in the lower-middle section of the screen. It remains inactive until valid credential formats are entered.
    *   **Secondary Action Button `[Crear clave de acceso]`**: Positioned below the primary login button. This button initiates the digital onboarding and credential creation process.
    *   **Onboarding Link `[Hazte cliente]`**: Located at the bottom center of the screen, designed for users who do not yet hold any BBVA products.

---

### 1.2 Detailed Operation & Edge Cases

#### 1.2.1 Account Onboarding Pathways

When a user taps `[Hazte cliente]`, they are directed to the account opening flow. The system supports two primary digital channels:

##### A. Mobile App Channel (Alta Inmediata)
*   **Estimated Duration**: 10 minutes.
*   **Step-by-Step Process**:
    1. Tap `[Hazte cliente]` on the login screen.
    2. Select the desired account type and tap `[Quiero mi cuenta ya]`.
    3. Review the system requirements and tap `[Empezar]`.
    4. Input a valid DNI/NIE and establish a 6-character alphanumeric access password.
    5. Input an email address and a Spanish mobile phone number, then tap `[Continuar]`.
    6. **Biometric Identity Verification**:
        *   Capture a clear photograph of the front and back of the identity document (DNI/NIE).
        *   Perform a facial selfie.
        *   Record a short video holding the identity document next to the face, speaking the prompted phrase clearly.
    7. Declare professional occupation and input personal details.
    8. Review the terms, conditions, and contract documents.
    9. Sign the contract by entering the 6-digit verification code received via SMS.

##### B. Web Channel (`bbva.es`)
*   **Estimated Duration**: 9 to 14 minutes.
*   **Step-by-Step Process**:
    1. Navigate to `bbva.es` and click `[Hazte cliente]` in the top right corner.
    2. Select the account type and click `[Abre tu cuenta...]`.
    3. Click `[Empezar]` after reading the initial instructions.
    4. Select the number of account holders (titulares) and click `[Siguiente]`.
    5. Define a username (DNI/NIE/TIE) and establish a 6-character alphanumeric access password.
    6. Input contact details.
    7. Upload clear front and back photographs of the identity document. If unavailable, documents can be emailed later to `altaclientes@bbva.com`.
    8. Declare economic activity and professional occupation.
    9. Input personal details.
    10. Select the identity verification method:
        *   **Videollamada (Video Call)**: Connect with an agent via a stable 4G/5G or Wi-Fi connection.
        *   **Número de cuenta (Existing IBAN)**: Provide an existing bank account number held at another Spanish financial institution.
        *   **Mensajero (Courier Service)**: Schedule a courier to physically collect signed contract documents.
    11. Review the contract documents and sign using the SMS verification code.

#### 1.2.2 Onboarding Rules for Foreign Nationals

Foreign nationals residing or non-residing in Spain must adhere to the following channel and documentation matrix:

| Document Type | Residency Status | Allowed Channels | Process Location & Finalization |
| :--- | :--- | :--- | :--- |
| **DNI** (Spanish National) | Resident in Spain | Web, App, or Branch | Fully digital or in-branch |
| **DNI** (Spanish National) | Non-Resident | Branch Only | Fully in-branch |
| **NIE** (EU Citizen) | Resident in Spain | Web, App, or Branch | Initiated online, finalized in-branch or fully in-branch |
| **TIE** (Non-EU Citizen) | Resident in Spain | Web, App, or Branch | Fully digital or in-branch |
| **Pasaporte** (EU / Non-EU) | Resident or Non-Resident | Branch Only | Fully in-branch |

*   **Age Requirement**: Applicants must be 18 years or older.
*   **Mobile Number Restriction**: A Spanish mobile phone number is mandatory. International phone numbers are blocked for onboarding and contract signing.
*   **Proof of Economic Activity**: Additional documentation (e.g., payroll/nómina, employment contract, or the latest IRPF tax return) may be requested during or after the process.

#### 1.2.3 Account Activation & Operational Timelines

An account is considered **operative** (capable of receiving transfers, supporting cash withdrawals, displaying movements, and processing direct debits) according to the following timelines:

```
[Onboarding Initiated]
       │
       ├─► Mobile App (with Video Call Verification) ──► IMMEDIATE ACTIVATION
       │
       └─► Web (bbva.es)
             │
             ├─► "Videollamada" (Video Call) ──────────► IMMEDIATE ACTIVATION
             │
             ├─► "Número de cuenta" (Existing IBAN) ───► 7 - 10 BUSINESS DAYS (Pending verification with origin bank)
             │
             └─► "Mensajero" (Courier Service) ────────► 7 - 10 BUSINESS DAYS (Pending physical contract signature)
```

*   **Document Pending Status**: If identity documents are missing or unreadable, they must be emailed to `altaclientes@bbva.com`. The account remains inactive until verified. Users can check pending document status by logging into `bbva.es` or the BBVA App.

#### 1.2.4 Credentials & Security Settings

*   **Username Rules**: Must be a NIF, NIE, DNI, or Passport number. Enter letters in uppercase, with no spaces or hyphens. Email addresses or phone numbers are not permitted as usernames.
*   **Password Rules**: Must be exactly 6 alphanumeric characters. No spaces or special symbols (`$`, `%`, `&`, `/`, etc.) are allowed.
*   **Biometric Access**: Fingerprint, FaceID, or Iris recognition can be enabled on compatible devices via the settings menu.
*   **Email Validation Procedure**: Validating the registered email address is a mandatory security requirement to receive official communications and transaction receipts.
    *   *Web Path*: Log into the Private Area on `bbva.es` > Click `[Mi Perfil]` (top right, next to "Salir") > Select `[Datos personales]` > Scroll to "Email" and click `[Opciones]` > Click `[Validar]` (or enter the email address twice if not registered, then click `[Validar]`) > Open the verification email received and click the confirmation link within **48 hours**.
    *   *Mobile App Path*: Log into the BBVA App > Open the lateral menu `[≡]` (top right) and select `[Perfil y ajustes]` (below the user's name) > Tap `[Email]` and select `[Opciones]` > Tap `[Validar]` on the "Email pendiente de validar" message (or enter the email address twice if not registered, then tap `[Validar]`) > Click the verification link in the email within **48 hours**.

#### 1.2.5 Fee Avoidance Framework (Elección Account)

The maintenance fee for the **Elección Account** can be reduced to **€0** by meeting specific criteria. Reviews are conducted monthly based on the preceding 4 calendar months.

##### Fee Tiers
*   **Tier 1 (€0/quarter)**: All primary requirements met.
*   **Tier 2 (€15/quarter - €60/year)**: Only "Income + 2 Payments" met.
*   **Tier 3 (€40/quarter - €160/year)**: Requirements not met.

##### Requirements for Private Customers

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      €0 FEE ELIGIBILITY PATHWAYS                        │
├─────────────────────────────────────────────────────────────────────────┤
│  Pathway A: Income + One Payment + One BBVA Product                     │
│  Pathway B: Savings Products Balance ≥ €25,000                          │
│  Pathway C: BBVA Shares Ownership ≥ 4,000 shares                        │
└─────────────────────────────────────────────────────────────────────────┘
```

1.  **Direct Deposit (Income)**: Must meet at least one of the following:
    *   *Payroll (Paycheck)*: > €800/month in at least 2 of the 4 calendar months preceding the review.
    *   *Pension / Unemployment Benefit*: > €300/month in at least 2 of the 4 calendar months preceding the review.
    *   *Periodic Payments*: > €800/month in at least 3 of the 4 calendar months preceding the review.
    *   *Pension Plan / Retirement Plan Income*: > €300/month in at least 3 of the 4 calendar months preceding the review.
2.  **Payments**: Must meet at least one of the following within the 4 calendar months preceding the review:
    *   *Direct Debits*: At least 5 debits charged to the account.
    *   *Credit Card Purchases*: At least 7 purchases made with a BBVA credit card linked to the account (counted when the transaction is posted).
3.  **BBVA Products**: Must hold at least one of the following:
    *   *Active Loan*: Up-to-date with payments in any of the 3 calendar months preceding the review.
    *   *Active Mortgage*: Up-to-date with payments in any of the 3 calendar months preceding the review.
    *   *Insurance Policy*: Active Life, Funeral, Health, Home, Car, or Business insurance sold by BBVA in at least 1 of the 3 calendar months preceding the review (excludes mini-insurance and Payment Protection Insurance).
    *   *Credit Card Spending*: An active BBVA credit card with a minimum expenditure of €200 within the 4 calendar months preceding the review.
    *   *Savings Products*: An average monthly balance > €5,000 in Investment Funds, ETFs, SICAVs (excluding open-ended companies), Pension Plans, Unit Linked policies, or eligible BBVA Annuities/Guaranteed plans. *Note: Employment Pension Plans are excluded.*

##### Alternative Pathways to €0 Fees
*   **Savings Balance**: Maintain a monthly average value > €25,000 in eligible savings products (Investment Funds, ETFs, Pension Plans, Unit Linked, or BBVA Annuities) in at least 2 of the 4 calendar months preceding the review.
*   **Share Ownership**: Hold a minimum of 4,000 BBVA shares deposited in a single securities account associated with the Elección Account in at least 1 of the 2 calendar months preceding the review.

##### Requirements for Self-Employed Customers (Autónomos)
1.  **Direct Deposit (Income)**: Receive at least **€600/month** in at least 3 of the 4 calendar months preceding the review via:
    *   Cash transfers or deposits.
    *   Check deposits, commercial documents, or trade credits.
    *   Remittance payments or farm payment orders.
    *   Factoring or reverse factoring income.
    *   POS (TPV) terminal income.
    *   Payments from a BBVA Personal or Employee Pension Plan.
2.  **Payments**: Must meet at least **two** of the following:
    *   *Social Security / Professional Association*: Monthly payments of ≥ €175 in at least 2 of the 4 calendar months preceding the review.
    *   *Payroll Payments*: Monthly paycheck payments of ≥ €600 to employees in at least 2 of the 4 calendar months preceding the review.
    *   *Tax Payments*: Monthly tax payments of ≥ €100 in at least 1 of the 3 calendar months preceding the review.
    *   *Direct Debits*: 5 direct debit charges within the 4 calendar months preceding the review.
    *   *Credit Card Purchases*: 7 purchases with a linked BBVA credit card within the 4 calendar months preceding the review.
3.  **BBVA Products / Alternative Pathways**: Same criteria as Private Customers (Active Loan, Mortgage, Insurance, Credit Card spending, Savings > €5,000, Savings > €25,000, or 4,000 BBVA shares).

---

## Section 2: Global Position & Primary Screen (Page 2)

### 2.1 Visual Layout & Topology

Upon successful authentication, the user is presented with the Global Position screen, which aggregates all active financial products.

```
┌────────────────────────────────────────────────────────┐
│ Hola Enrique                                     ?   ≡ │
├────────────────────────────────────────────────────────┤
│  ┌──────────────────────┐    ┌──────────────────────┐  │
│  │ •••• €               │    │ •••• €               │  │
│  │ Ver patrimonio       │    │ Ver gastos           │  │
│  └──────────────────────┘    └──────────────────────┘  │
├────────────────────────────────────────────────────────┤
│ CUENTAS                                         •••• € │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Ir a análisis de gastos                        > │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Cuenta *9880                                 ••••│  │
│  │ • 9880                            Disponible     │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Cuenta *3345                                 ••••│  │
│  │ • 3345                            Disponible     │  │
│  └──────────────────────────────────────────────────┘  │
├────────────────────────────────────────────────────────┤
│ TARJETAS                                               │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Tarj. débito *2852                               │  │
│  │ (((•))) 2852                                     │  │
│  └──────────────────────────────────────────────────┘  │
├────────────────────────────────────────────────────────┤
│  [Inicio]   [Salud Fin...]   [Contratar]   [Buzón]   [Gestor] │
└────────────────────────────────────────────────────────┘
```

*   **Top Greeting & Utility Bar**:
    *   **Greeting Text**: "Hola [User Name]" (e.g., "Hola Enrique") located at the top left.
    *   **Help Button `[?]`**: Located to the left of the menu icon. Tapping this launches the "Blue" virtual assistant.
    *   **Lateral Menu Button `[≡]`**: Located at the top right corner.
*   **Financial Health Summary Cards**:
    *   **Assets Card `[Ver patrimonio]`**: Displays the total net worth (masked by default as `•••• €`).
    *   **Expenses Card `[Ver gastos]`**: Displays the total expenses for the current month (masked by default as `•••• €`).
*   **Accounts Section ("CUENTAS")**:
    *   **Analysis Link `[Ir a análisis de gastos]`**: Positioned directly below the section header.
    *   **Account Cards**: Individual cards for each active account (e.g., `[Cuenta *9880]` and `[Cuenta *3345]`). Each card displays the masked balance, the last four digits of the account number, and the "Disponible" (Available) status.
*   **Cards Section ("TARJETAS")**:
    *   **Card Cards**: Individual cards for active cards (e.g., `[Tarj. débito *2852]`), displaying a contactless icon and the last four digits of the card number.
*   **Bottom Navigation Bar**:
    *   **Home Icon `[Inicio]`**: Returns the user to the Global Position screen.
    *   **Heart Icon `[Salud Financiera]`**: Opens the financial health analysis dashboard.
    *   **Plus Icon `[Contratar]`**: Opens the product catalog to apply for new accounts, cards, loans, or insurance.
    *   **Envelope Icon `[Buzón]`**: Opens the secure message center for notifications and official communications.
    *   **User Icon `[Gestor]`**: Opens the remote personal banking support interface ("Gestor Contigo").

---

### 2.2 Detailed Operation & Edge Cases

#### 2.2.1 "Apartados" (Sub-Accounts / Savings Spaces)

"Apartados" is an in-app tool that allows users to partition funds within an existing bank account without contracting additional financial products.

*   **Key Features**:
    *   *Manual Contributions*: Users can add or return money to the main account balance instantly.
    *   *Payment Isolation*: Funds held in an "Apartado" are excluded from the "available balance" shown in the global position. They cannot be used for card payments or transfers.
    *   *Auto-Disbursement Safeguard*: If the main account balance is insufficient to cover mandatory payments (e.g., loans, mortgages, or direct-debited bills), the system automatically withdraws the required amount from the "Apartado".
    *   *Visual Representation*:
        *   **Actual Balance**: Includes the main account balance + "Apartados" balance (visible on Web and to branch/phone agents under "Retenciones").
        *   **Available Balance**: Main account balance only (visible in the app's global position).
*   **Creation Process**:
    1. Select the source account from the Global Position.
    2. Tap the option to create an "Apartado".
    3. Define a custom **Name** for the space.
    4. Specify the initial **Amount** to transfer.
*   **Channel Capabilities**:

| Action | App | Web | Branch / Phone |
| :--- | :---: | :---: | :---: |
| Create / Delete Apartado | Yes | No | No |
| Add / Return Funds | Yes | No | No |
| View Total Balance (incl. Apartados) | Yes | Yes | Yes (under "Retenciones") |
| Edit Apartado Name | Yes | No | No |

#### 2.2.2 Non-Client App Capabilities

Non-clients can register as "Users" for free to access specific tools without opening an account.

*   **Available Features**:
    *   *Pedir cita*: Schedule in-person or telephone appointments with BBVA agents.
    *   *Tramitar herencias*: Manage inheritance procedures for deceased BBVA clients.
    *   *Servicio de Agregación*: Connect and view accounts and financial products from other banks in a single interface.
    *   *Compartir gastos*: Split expenses with contacts (including non-clients).
    *   *Pagar recibos*: Pay non-direct debited bills and taxes using a non-BBVA card.
    *   *Iniciación de Pagos*: Initiate transfers from aggregated external accounts within the BBVA interface under PSD2 security standards.
    *   *Mi día a día*: Categorize income and expenses to analyze personal finances.
    *   *BBVA Valora*: Estimate property valuations and analyze regional real estate prices.
    *   *Espacio hipoteca*: Track mortgage applications, upload study documents, and contact assigned managers.
    *   *Calculators*: Access net salary and fuel consumption calculators.
*   **Registration Process**:
    1. Download and open the BBVA App.
    2. Select the option to register as a user.
    3. Input a valid email address.
    4. Provide contact details and set credentials:
        *   *Username*: DNI or TIE.
        *   *Access Password*: 4 to 6 alphanumeric characters (no symbols).
    5. Accept the terms and conditions.
    6. Input and confirm personal details (First Name, Last Name).

#### 2.2.3 Professional Collectives Space (Espacio Colectivos)

The "Espacio Colectivos" is a dedicated section within the BBVA App offering preferential financial conditions (e.g., discounted mortgages, loans) to members of professional collectives with active BBVA agreements.

*   **Eligible Collectives**: State Security Forces (National Police, Civil Guard, regional police forces), public and private school teachers, medical professionals, healthcare staff, and employees of corporate clients or public administrations.
*   **Access & Verification Process**:
    1. *Verification*: Contact a BBVA manager or visit a branch to verify if your collective has an active agreement.
    2. *Accreditation*: Provide proof of membership (e.g., a recent payroll slip or official professional credential).
    3. *App Access*: Once registered by an agent, log into the BBVA App, navigate to the `[Experiencias]` section, and select `[Espacio Colectivos]` to view tailored offers.

---

## Section 3: Navigation, Menus & Quick Actions (Page 3)

### 3.1 Visual Layout & Topology

This section details the primary navigation patterns: the horizontal swipe menu (Menú de operaciones), the product details screen (Menú de productos), the sidebar menu (Menú lateral), and the virtual assistant interface (Botón de ayuda).

```
┌────────────────────────────────────────────────────────┐
│  SWIPE MENU (Menú de operaciones)                      │
│  ┌──────────────────────────────────────────────────┐  │
│  │ Cuenta *3345                                     │  │
│  ├──────────────────────────────────────────────────┤  │
│  │ [Mostrar más]   [bizum Enviar...]   [Transfer...]│  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│  SIDEBAR MENU (Menú lateral)                           │
│  Enrique                                               │
│  Perfil                                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │ [Configuración]                                  │  │
│  │ [Seguridad y privacidad]                         │  │
│  │ [Sostenibilidad]                                 │  │
│  │ [Hacer una operación]                            │  │
│  │ [Experiencias]                                   │  │
│  │ [Oficinas y cajeros]                             │  │
│  │ [Promos y utilidades]                            │  │
│  │ [Valorar la app]                                 │  │
│  │ [Acerca de]                                      │  │
│  ├──────────────────────────────────────────────────┤  │
│  │ [Salir]                                          │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│  BLUE ASSISTANT                                  i   X │
│  ¡Hola, Enrique!                                       │
│  Soy Blue, tu asistente virtual de BBVA.               │
│  ┌──────────────────────────────────────────────────┐  │
│  │ [¿Qué sabes hacer Blue?]                         │  │
│  │ [Preguntas frecuentes que te pueden ayudar]      │  │
│  └──────────────────────────────────────────────────┘  │
│  ┌───────────────────────────────────────────────┬──┐  │
│  │ Escribe un mensaje                            │🎙️│  │
│  └───────────────────────────────────────────────┴──┘  │
└────────────────────────────────────────────────────────┘
```

*   **Horizontal Swipe Menu (Menú de operaciones)**:
    *   Triggered by swiping left on any product card (e.g., an account) in the Global Position.
    *   Reveals quick action buttons: `[Mostrar más]` (Show more), `[bizum Enviar/Recibir dinero]` (Send/Receive money via Bizum), and `[Transferencias / Traspasos]` (Transfers).
*   **Product Details Screen (Menú de productos)**:
    *   Triggered by tapping directly on a product card.
    *   Displays detailed balances: "Saldo disponible" (Available balance) and "Saldo actual" (Actual balance).
    *   Includes a `[Más información]` link and a `[Movimientos previstos]` (Predicted movements) section.
    *   Provides a horizontal quick-action bar containing: `[Buscar movimientos]` (Search movements), `[Transferencias / Traspasos]`, `[bizum Enviar/Recibir dinero]`, and `[Mostrar más]`.
    *   Displays a chronological list of "MOVIMIENTOS" (Transactions) with date and category.
*   **Sidebar Menu (Menú lateral)**:
    *   Accessed by tapping the `[≡]` icon at the top right of the screen.
    *   Contains the following navigation links:
        *   `[Configuración]`: Profile settings, notifications, and biometric configuration.
        *   `[Seguridad y privacidad]`: Password management, card blocking, and privacy settings.
        *   `[Sostenibilidad]`: Carbon footprint calculator and sustainable product offers.
        *   `[Hacer una operación]`: Direct access to transfers, Bizum, bill payments, and mobile cash.
        *   `[Experiencias]`: Access to specialized spaces like "Espacio Colectivos".
        *   `[Oficinas y cajeros]`: Interactive map to locate physical branches and ATMs.
        *   `[Promos y utilidades]`: Commercial promotions and utility tools.
        *   `[Valorar la app]`: App store rating link.
        *   `[Acerca de]`: Legal information and app version details.
        *   `[Salir]`: Securely logs the user out of the application.
*   **Help Button Interface (Blue Assistant)**:
    *   Accessed by tapping the `[?]` icon in the top bar.
    *   Displays a greeting and quick-help buttons: `[¿Qué sabes hacer Blue?]` and `[Preguntas frecuentes que te pueden ayudar]`.
    *   Features a text input field `[Escribe un mensaje]` at the bottom, paired with a microphone icon `[🎙️]` for voice commands.

---

### 3.2 Detailed Operation & Edge Cases

#### 3.2.1 Standard & Immediate Transfers

Transfers can be executed via Web, App, or ATMs.

##### Transfer Types & Timelines
*   **Standard National / SEPA Transfers**: Arrive at the destination account within 1 business day. If the order is placed after **16:30**, it is processed on the next business day.
*   **Immediate Transfers**: Arrive at the destination account within seconds. Available 24/7.
*   **International Transfers (Non-SEPA)**: Typically take up to 48 hours to process.
*   **Internal Transfers (Traspasos)**: Processed instantly on the same day.

##### Standard Limits
*   **Per Operation**: Max €15,000.
*   **Daily Limit**: Max €30,000.
*   *Note*: Transfers between accounts held by the same individual have no limit, up to the available balance.

##### Modifying Transfer Limits
*   *In-App/Web*: Users can lower their transfer limits at any time to enhance security.
*   *Temporary Increases*: Users can temporarily increase their immediate transfer limit up to their daily limit for a single transaction. This temporary limit expires after the transaction is completed or within a maximum of 2 days.
*   *Transaction Rules*: Only one daily transfer exceeding €1,000 is permitted. For transactions under €1,000, users can perform unlimited operations up to a daily cap of €5,000.
*   *Alternative Channels*: Limit modifications can also be requested via a BBVA manager, at a branch, or through the "Línea BBVA" telephone service.

##### Step-by-Step Transfer Process (Mobile App)
1. Tap `[Hacer una operación]` > `[Transferencias]` (or tap `[Transferencias / Traspasos]` from the product quick actions).
2. Select the source account, then input the destination IBAN and recipient's name.
3. Input the amount.
4. Select `[Transferencia inmediata]` or standard transfer, then tap `[Continuar]`.
5. Input the concept and tap `[Continuar]`.
6. Review the transaction summary and tap `[Continuar]`.
7. Enter the SMS verification code and tap `[Aceptar]`.

##### Step-by-Step Transfer Process (Web Channel)
1. Log into `bbva.es`.
2. Select the source account and click `[Quiero]` > `[Realizar transferencias/traspasos]`.
3. Select the transfer type (Standard or Immediate) and click `[Comenzar]`.
4. Input the recipient's IBAN and full name, then click `[Continuar]`.
5. Input the amount and concept, then click `[Continuar]`.
6. Select the execution date and delivery speed.
7. Review the details.
8. Enter the SMS verification code to authorize the transaction.
9. Download the transaction receipt as a PDF if required.

##### Reusing a Transfer
To repeat a previous transfer without re-entering details:
1. Log into `bbva.es`.
2. Hover over the source account, click `[Quiero]`, and select `[Realizar transferencias / traspasos]`.
3. Select `[Reutilizar transferencias]`.
4. Use the search bar to find the transaction by recipient name, alias, or concept, then select it to pre-fill the form.

##### Transfer Notifications (SMS/Email)
During the transfer process, users can configure free notifications for the recipient:
*   **SMS Notification**: Enter the recipient's mobile number. The SMS is sent free of charge once the transfer is authorized.
*   **Email Notification**: Enter the recipient's email address. BBVA sends an official confirmation email on your behalf.
*   *Note*: Notifications are only dispatched after the transfer is signed with the SMS security code. For frequent recipients, the system may bypass the SMS signature step, displaying an orange notification: *"La cuenta a la que vas a enviar dinero es una de tus habituales..."*

#### 3.2.2 Bizum Operations

Bizum is an instant mobile-to-mobile payment service. By design, a mobile phone number can only be linked to a single bank account (IBAN) at any given time. However, multiple phone numbers can be linked to the same IBAN.

##### Limits

| Category | Per Operation | Daily Limit | Monthly Limit |
| :--- | :--- | :--- | :--- |
| **Particulars (Individuals)** | €0.50 to €1,000 | €2,000 | €5,000 |
| **ONGs (Donations)** | €0.50 to €1,000 | €2,000 | €5,000 |
| **Compras Online (E-commerce)** | From €0.01 | €3,000 | €5,000 |

*   **Reception Limits**: Individuals can receive a maximum of **60 Bizum transactions per day** and **60 Bizum transactions per month**. If the monthly cap of 60 transactions is reached in a single day, no further transactions can be received for the remainder of that calendar month. *Note: These limits do not apply to registered ONGs.*

##### Registration Process (Mobile App)
1. Open the menu, tap `[Hacer una operación]`, and select `[Bizum]`.
2. Select the bank account to link with Bizum and tap `[Comenzar]`.
3. Verify your details and tap `[Aceptar y continuar]`.
4. Enter the SMS verification code and tap `[Aceptar]`.

##### Registration Process (Web Channel)
1. Log into `bbva.es`.
2. Navigate to `[Posición Global]` and select `[Bizum]`.
3. Click `[Aceptar]`.
4. Enter the verification code sent via SMS to your registered mobile number.
5. Click `[Finalizar]`.

##### Changing Bizum Accounts from Another Bank
To transfer an active Bizum service from another financial institution to BBVA:
1. Log into the app of the current bank, navigate to Bizum settings, and select `[Darse de baja]` (Unregister) to unlink the phone number.
2. Log into the BBVA App and complete the Bizum registration process using the same phone number.

##### Updating Your Phone Number in Bizum
If you change your mobile number, you must update your bank profile before registering the new number with Bizum:
1. Log into `bbva.es`.
2. Go to `[Mi Perfil]` (top right) > `[Datos Personales]`.
3. Locate the active number under "Teléfonos" and click `[Eliminar]`.
4. Visit a BBVA branch or ATM to register and validate your new mobile number. Once updated, the new number will appear in your online profile.
5. Complete the Bizum registration process in the BBVA App using the new number.

##### Cancellation and Reclaim Policies
*   **Cancellation**: Once a Bizum payment is sent, it is processed within 5 seconds and **cannot be canceled** or recalled through the app.
*   **Reclaim Options**:
    *   *Registered Recipients*: Contact the recipient directly to request a refund. The recipient can return the funds by selecting the transaction in their history and tapping `[Devolver]`.
    *   *Unregistered Recipients*: If the recipient is not registered on Bizum, they receive an SMS invitation to sign up. If they do not register within **2 days**, the transaction is automatically canceled, and the funds are returned to the sender's account.
    *   *Disputes*: If a recipient refuses to return an accidental payment, the sender must contact BBVA customer support for further instructions.

##### International Bizum Payments
*   **EuroPA Alliance**: Bizum supports instant cross-border payments between Spain, Portugal, Andorra, and Italy through interoperability with regional payment networks (MB Way in Portugal, Bancomat Pay in Italy). This network connects over 120 million users across 16 participating banks, including BBVA.
*   **Other Countries**: You can send a Bizum to a contact in any country outside the EuroPA Alliance, provided the recipient's phone number is registered with Bizum and linked to a Spanish bank account.

##### Donations via Bizum
Users can make secure donations to over 1,500 registered non-governmental organizations (ONGs).
1. Open the BBVA App and select `[Aportar a una causa solidaria]` within the Bizum menu.
2. Select an organization from the list or enter the unique **Código ONG** (5-digit code).
3. Input the donation amount and confirm the transaction.
4. **Tax Certificates**: To request a donation certificate for tax deductions, email the recipient ONG with the following details: Full Name, DNI/NIE, Postal Address, Email Address, and the exact donation amount and date.

##### Sending Money to Unregistered Contacts
*   **Payments**: The recipient receives an SMS notification with an invitation to register. If they do not register within **2 days**, the transaction is canceled and no funds leave the sender's account.
*   **Requests**: The recipient receives an SMS invitation. If they register within **2 days**, the request is delivered. They then have **7 days** to accept or reject the request before it expires.

---

## Section 4: Tools, Features & Cards Portfolio (Page 4)

### 4.1 Visual Layout & Topology

This screen highlights the core payment, card control, and daily management tools available within the application.

```
┌────────────────────────────────────────────────────────┐
│ Paga, cobra y controla tus tarjetas                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │ [Pago móvil]                                   > │  │
│  │ [Bizum]                                        > │  │
│  │ [Apaga o enciende tarjetas]                    > │  │
│  │ [Efectivo móvil]                               > │  │
│  └──────────────────────────────────────────────────┘  │
│ Gestiona tu día a día                                  │
│  ┌──────────────────────────────────────────────────┐  │
│  │ [Suma seguridad en todo lo que hagas]          > │  │
│  │ [Notificaciones push]                          > │  │
│  │ [Movimientos categorizados]                    > │  │
│  │ [Pago de recibos y tributos]                   > │  │
│  │ [Cumple con tus valores de sostenibilidad]     > │  │
│  └──────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────┘
```

*   **Payment & Card Control Group ("Paga, cobra y controla tus tarjetas")**:
    *   `[Pago móvil]`: Configures mobile contactless payments.
    *   `[Bizum]`: Direct access to the Bizum payment interface.
    *   `[Apaga o enciende tarjetas]`: Allows users to instantly lock (turn off) or unlock (turn on) their cards.
    *   `[Efectivo móvil]`: Generates a code to withdraw cash from an ATM without a physical card.
*   **Daily Management Group ("Gestiona tu día a día")**:
    *   `[Suma seguridad en todo lo que hagas]`: Configures biometric signatures for authorizing operations.
    *   `[Notificaciones push]`: Configures real-time push alerts for account and card movements.
    *   `[Movimientos categorizados]`: Displays categorized income and expenses.
    *   `[Pago de recibos y tributos]`: Interface for paying non-direct debited bills and taxes.
    *   `[Cumple con tus valores de sostenibilidad]`: Displays carbon footprint calculations and environmental impact metrics.

---

### 4.2 Detailed Operation & Edge Cases

#### 4.2.1 Mobile Payments & Contactless (NFC)

*   **Setup and Verification**:
    1. Ensure your mobile device has **NFC** enabled in its system settings.
    2. Link your BBVA Visa or Mastercard to your mobile wallet (Apple Pay, Google Pay, or Samsung Pay) via the BBVA App.
    3. Verify that the merchant's POS terminal (datáfono) supports contactless payments.
    4. **Security**: For transactions exceeding contactless limits, or as required by security protocols, you must enter your card's secret PIN on the merchant's POS terminal.

#### 4.2.2 Card Portfolio & Operations

BBVA offers credit, debit, and prepaid cards, including the **Aqua** range, which features enhanced security with no printed card numbers (PAN) and a dynamic CVV.

##### Credit Cards

| Card Name | Credit Limit / Features | Insurance Included | Foreign Transaction Fees |
| :--- | :--- | :--- | :--- |
| **Aqua Más** | Defer payments > €50 over 3 months at 0% NIR/APR. | Online purchase protection. | First €300/month fee-free; 3% thereafter. |
| **Aqua Más Young** | For ages 18–29. No issue/maintenance fees. | Travel assistance. | Fee-free spending and ATM withdrawals abroad. |
| **Aqua Máxima** | 10% cashback on eligible subscriptions (Netflix, Spotify, etc.). | Comprehensive travel insurance. | Fee-free spending and ATM withdrawals abroad. |
| **Después Gold** | Credit limit up to €30,000. | Accident and travel insurance. | First €300/month fee-free; 3% thereafter. |
| **A Tu Ritmo Revolving** | Revolving deferred payment. No issue/maintenance fees. | Basic coverage. | First €300/month fee-free; 3% thereafter. |
| **Visa Platinum** | High credit limit. | Accident (€1.25M) and ATM robbery insurance. | First €300/month fee-free; 3% thereafter. |
| **VIA-T** | Electronic toll payment (Spain, France, Portugal). | N/A | N/A |
| **Renfe Dorada** | For ages 60+. Up to 40% discount on Renfe tickets. | Basic travel insurance. | First €300/month fee-free; 3% thereafter. |
| **Viajes Card+** | Optimized for international travel. | Trip cancellation and lost luggage. | Reduced international fees. |
| **Iberia Classic** | Earns 1 Avios per €5 spent. 10% discount on Iberia flights. | Standard flight insurance. | First €300/month fee-free; 3% thereafter. |
| **Iberia Icon** | Earns 1 Avios per €3 spent. Preferential boarding. | Extensive travel coverage. | First €300/month fee-free; 3% thereafter. |
| **Infinite Visa** | Premium lifestyle benefits and hotel discounts. | Maximum coverage package. | First €300/month fee-free; 3% thereafter. |

##### Premium & Private Banking Credit Cards
*   **BBVA Infinite Patrimonios**: No annual fee. Includes €1.5M travel accident insurance, 0% currency exchange fees, 0% cash withdrawal fees abroad, and a Priority Pass for VIP airport lounges.
*   **Private Banking Platinum**: No annual fee. Includes €1.25M accident insurance, travel assistance, and 0% currency exchange/cash withdrawal fees abroad.
*   **Aqua Gold Personal Banking**: No annual fee. Includes €760,000 travel accident insurance, travel assistance, and the *Pack Viajes Esencial* (fee-free spending in foreign currencies up to €300/month).
*   **Private Banking Infinite**: Includes €1.5M travel accident insurance, 0% currency exchange/cash withdrawal fees abroad, and 4 free VIP airport lounge visits per year.
*   **Infinite Personal Banking**: Includes €1.5M travel accident insurance, 0% currency exchange/cash withdrawal fees abroad, and VIP lounge access in the event of flight delays.
*   **Platinum Personal Banking**: Includes €1.25M accident insurance, travel assistance, and 0% currency exchange/cash withdrawal fees abroad.

##### Debit Cards
*   **Aqua Debit**: Features a dynamic CVV and no printed numbers. Includes instant transaction alerts.
*   **Aqua Debit for Young People**: For ages 18–29. No issue or maintenance fees. Offers reduced fees on international transactions.
*   **Aqua Máxima Debit**: Includes 10% cashback on eligible digital subscriptions and fee-free spending abroad.
*   **Aqua Debit for Minors**: For ages 12–17. Linked to a parent/guardian account for real-time monitoring. Features €0 issuance/maintenance fees and a free Travel Pack.

##### Prepaid Cards
*   **Aqua Prepaid**: Features a dynamic CVV and no printed numbers. Supports unlimited fee-free top-ups.
*   **Virtual Card**: Designed for online shopping without a physical card. Features €0 issue and maintenance fees.

#### 4.2.3 Foreign Currency Transactions & Travel Packs

*   **Standard Foreign Currency Fees**: For purchases in currencies other than the Euro, no commission is charged on the first **€300 per month** of spending. A **3% commission** is applied to the equivalent Euro amount for monthly spending exceeding €300, as well as for all cash withdrawals abroad.
*   **Pack Viajes Plans**: To bypass standard international limits, users can activate a **Pack Viajes** plan starting from **€2.99/month**. These plans increase foreign currency spending limits and allow fee-free cash withdrawals abroad. Plans can be turned on or off instantly via the BBVA App.

#### 4.2.4 Prepaid Card Loading & Management

Prepaid cards must be loaded with funds before use.

*   **Loading Limits**:
    *   *Standard Prepaid Cards*: Top-up amount between **€6 and €600**.
    *   *Aqua Prepaid Card*: Top-up amount between **€6 and €1,000**.
*   **Top-Up Channels**: Top-ups can be performed free of charge via the BBVA App, `bbva.es`, BBVA ATMs, branches, or by calling customer service at `900 102 801`.

#### 4.2.5 PIN Management & Card Delivery Tracking

##### Consulting Your Card PIN (Web Channel)
1. Log into `bbva.es`.
2. Select the card and click `[Quiero]` > `[Consultar PIN]`.
3. Enter the SMS verification code sent to your mobile.
4. The PIN will be displayed on screen for **30 to 60 seconds**.

##### Consulting Your Card PIN (Mobile App Channel)
1. Select the card from the Global Position.
2. Tap `[Mostrar más]` > `[Consultar PIN]`.
3. Enter the SMS verification code.
4. The PIN will be displayed on screen for **10 seconds**.

##### Changing Your Card PIN
*   *Via App*: Select the card, tap `[Mostrar más]` > `[Cambiar PIN]`, and enter your new 4-digit code.
*   *In-Branch*: Visit a BBVA branch with your physical card and valid ID (DNI/Passport). An agent will provide a one-time code to enter at a branch ATM to set your new PIN.

##### Card Delivery & Tracking
New cards are mailed to the user's registered address within a few days of account activation. The card PIN is sent separately via SMS.
*   *Tracking Card Status*: Log into `bbva.es` or the BBVA App, navigate to the "Tarjetas" (Cards) section, and view the card status, which will display one of the following states: **Alta** (Registered), **En Fabricación** (In Production), or **Enviada** (Shipped). Confirm the displayed shipping address is correct.

#### 4.2.6 Payment of Non-Direct Debited Bills (Debit Entries)

Both clients and non-clients can pay non-direct debited bills, local taxes, and "Pagos Express" products through BBVA's digital channels or ATM network.

*   **Payment Methods**:
    *   *BBVA Clients*: Can pay directly from their account or using a linked credit/debit card via `bbva.es` or the BBVA App.
    *   *Non-Clients*: Can pay using any valid debit or credit card via the BBVA website or at BBVA ATMs.
    *   *Direct-Debit Verification*: Users can verify the details of a direct-debit charge by entering the exact bill amount, due date, and the unique statement code in the "Detail of the debit entry" tool on the BBVA website.

#### 4.2.7 Cybersecurity Best Practices

##### The "3Ps" Security Rule
To protect against social engineering attacks, users should apply the **3Ps Rule**:
1.  **Prudencia (Prudence)**: Be skeptical of unexpected communications, especially those offering refunds or demanding urgent action. Check for generic greetings (e.g., messages not addressed to you by name) and suspicious sender addresses.
2.  **Pensar antes de actuar (Think before acting)**: Do not click on links in SMS messages or emails. BBVA does not include links in its transactional SMS communications. If in doubt, type the official URL directly into your browser.
3.  **Proteger la información (Protect your information)**: Never share passwords, card PINs, or personal details. If a website or caller requests extensive personal or card information, terminate the interaction immediately.

##### Common Social Engineering Attacks
*   **Phishing**: Fraudulent emails designed to steal credentials or deliver malware. Always check the sender's domain and look for spelling or formatting errors.
*   **Smishing**: Fraudulent SMS messages containing links to spoofed websites. BBVA will never send links via SMS to request credentials.
*   **Vishing**: Fraudulent phone calls where attackers pose as bank staff or technical support. If you receive a suspicious call, hang up and call BBVA directly at `900 102 801`.

##### Device Security
*   Install and maintain reputable antivirus software on all devices.
*   Only download official apps from recognized stores (Google Play Store, Apple App Store).
*   Keep your operating system and applications updated to the latest version.
*   **Two-Factor Authentication (2FA)**: Enable 2FA on all compatible services. This requires entering a temporary code (sent via SMS or generated by an authenticator app) in addition to your password to access your account.

---

## Section 5: Financial Health, Decisions & Time Saving (Page 5)

### 5.1 Visual Layout & Topology

This screen focuses on financial planning, decision-making tools, and time-saving features.

```
┌────────────────────────────────────────────────────────┐
│ Controla tu salud financiera                           │
│  ┌──────────────────────────────────────────────────┐  │
│  │ [Movimientos previstos]                        > │  │
│  │ [Marca objetivos de ahorro]                    > │  │
│  │ [Estate al día de tus recibos y suscripciones] > │  │
│  └──────────────────────────────────────────────────┘  │
│ Toma mejores decisiones                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │ [Valora casa]                                  > │  │
│  │ [Valora Coche]                                 > │  │
│  │ [Mis viajes]                                   > │  │
│  └──────────────────────────────────────────────────┘  │
│ Ahorra tiempo                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │ [Cita previa]                                  > │  │
│  │ [Turno de caja digital]                        > │  │
│  │ [Mis Conversaciones]                           > │  │
│  └──────────────────────────────────────────────────┘  │
│                                                        │
│ Y si todavía quieres saber más entra desde [aquí]...   │
└────────────────────────────────────────────────────────┘
```

*   **Financial Health Group ("Controla tu salud financiera")**:
    *   `[Movimientos previstos]`: Displays estimated future income and expenses.
    *   `[Marca objetivos de ahorro]`: Sets spending limits and schedules periodic savings contributions.
    *   `[Estate al día de tus recibos y suscripciones]`: Manages recurring bills and digital subscriptions.
*   **Decision Support Group ("Toma mejores decisiones")**:
    *   `[Valora casa]`: Real estate valuation tool to compare buying vs. renting.
    *   `[Valora Coche]`: Estimates the value of second-hand cars.
    *   `[Mis viajes]`: Budgeting and expense tracking tool for vacations.
*   **Time Saving Group ("Ahorra tiempo")**:
    *   `[Cita previa]`: Schedules appointments with a personal manager.
    *   `[Turno de caja digital]`: Reserves a digital turn at a physical branch cashier.
    *   `[Mis Conversaciones]`: Secure chat interface with your assigned manager.
*   **External Link**:
    *   `[aquí]`: Hyperlink directing users to the main BBVA website for additional information.

---

### 5.2 Detailed Operation & Edge Cases

#### 5.2.1 Financial Health Framework

##### The 50/30/20 Budgeting Rule
This rule helps individuals manage their annual household income effectively:
*   **50% (Needs)**: Allocated to essential living expenses (housing, utilities, education, groceries).
*   **30% (Wants)**: Allocated to non-essential lifestyle expenses (dining out, hobbies, travel, entertainment).
*   **20% (Savings)**: Dedicated to building an emergency fund, investing, or long-term financial goals.

##### Debt Management
*   **Debt-to-Income Ratio**: To maintain healthy finances, total monthly debt payments (including mortgages, personal loans, and credit cards) should not exceed **35% to 40%** of net monthly income.

##### Net Worth Calculation
Calculating your net worth provides a clear picture of your overall financial health.

$$\text{Net Worth} = \text{Total Assets} - \text{Total Liabilities}$$

*   **Total Assets**: The sum of cash in bank accounts, property valuations, and investment portfolios.
*   **Total Liabilities**: The sum of outstanding debts, including mortgages and loans.
*   **Analysis**: A positive, growing net worth indicates healthy financial progress. A negative net worth suggests the need for financial adjustments.

#### 5.2.2 Gestor Contigo (Remote Personal Banking Support)

The **Equipo Contigo** is a team of over 1,400 remote banking managers who provide personalized financial support without requiring clients to visit a physical branch.

*   **Key Services**:
    *   *Complex Transactions*: Assistance with mortgages, personal loans, investment funds, pension plans, and insurance policies.
    *   *Daily Operations*: Support for account queries, card management (e.g., adjusting spending limits, canceling lost cards), and resolving transaction issues.
    *   *Availability*: The core team is available during standard business hours. For urgent issues outside these hours or on weekends, an Emergency Team is available 24/7.
*   **Accessing Your Manager**:
    *   *Web Channel*: Log into `bbva.es` > Go to your Posición Global and click `[Mi Gestor]` in the top menu.
    *   *Mobile App Channel*: Log into the BBVA App > Tap `[Mi Gestor]` (bottom right) to view contact options.
*   **Security & Verification**:
    *   *In-App Calling*: Calling your manager directly through the BBVA App automatically authenticates your identity, bypassing the need to enter access codes.
    *   *Standard Phone Calls*: If calling from a standard phone line, you will be prompted to enter your multi-channel access code.
    *   *Voice Biometrics*: Clients can set up voice recognition, which uses a unique vocal print to verify identity securely without requiring passwords.

#### 5.2.3 Business Financial Services

##### Confirming for Providers
Confirming allows providers to manage and accelerate the collection of invoices issued to corporate clients.

###### Workflow for BBVA Clients
1. Log into the BBVA Business Portal.
2. Navigate to **"Cobros"** > **"Confirming"**.
3. Select the company's **CIF** and choose the client to view pending invoices.
4. Select your preferred **Anticipo** (Advance) modality:
    *   *Puntual*: Manually select which invoices to advance in each order.
    *   *Automática*: All incoming invoices from the selected client are financed automatically upon receipt.
5. Review, accept, and sign the contract.

###### Simulating an Invoice Advance
1. Go to **"Cobros"** > **"Confirming Proveedores"** > **"Facturas"** > **"Solicitar"**.
2. Select invoices with an **"Anticipable"** status and click **"Simular anticipo"**.
3. Review the simulated net payout (after fees and interest). If acceptable, click **"Solicitar anticipo"** to finalize.

###### Workflow for Non-Clients
Non-clients must register in the **Espacio Confirming** within the private area for non-clients on `bbva.es`.
1. Log into the **Espacio Confirming**.
2. Go to the **"Contratos clientes"** tab.
3. Select the client from the list, click the three dots on the right, and select **"Firmar contrato"**.
4. Choose your preferred advance modality:
    *   *Automático*: Invoices are advanced automatically upon receipt.
    *   *Puntual*: Manually select and confirm invoices under **"Anticipos"** > **"Simular/Solicitar"** > **"Confirmar la solicitud"**.
5. Download and read the contract document.
6. Enter the verification code received via SMS to sign the contract.

##### API Confirming Remittances
The **Confirming Remittances API** allows businesses to integrate BBVA's confirming services directly into their internal ERP or billing systems, eliminating manual file exchanges.
*   *Key Capabilities*: Process automation, embedded financing, limit optimization, real-time error resolution, and secure connection (no manual signatures required for individual files).

```
[ERP / Internal System]
         │
         ├─► 1. Onboard Provider ────────► Send provider details via API
         │                                  (BBVA notifies when contract is signed)
         │
         ├─► 2. Simulate / Quote ────────► Request real-time pricing for selected invoices
         │
         └─► 3. Submit Remittance ───────► Transmit invoice batch and payment instructions
                                            (Receive instant confirmation of processing status)
```

##### Online Business Registration (Alta Online Empresas)
Businesses can open a BBVA Business Account (such as the *Cuenta Bienvenida para Empresas*) online.
*   *Eligibility Criteria*: The company's **CIF** must begin with **A** (Sociedad Anónima) or **B** (Sociedad Limitada). The company must be managed by a **Sole Administrator** (Administrador Único) or **Joint Administrators** (Administradores Solidarios) who are tax residents in Spain.
*   *Technical Setup*:
    *   A valid **Digital Certificate** for the Sole or Joint Administrator issued by the FNMT or Izenpe. Alternatively, a representative certificate for a legal entity with joint signature authority is accepted.
    *   **Autofirma Software** (version 1.7 or higher) installed on the computer.
    *   *Exception*: Existing BBVA personal clients can complete the process using their online banking credentials, bypassing the need for Autofirma and digital certificates.
*   *Required Documentation*: Valid **DNI/NIE** of the administrator(s) in `.jpg` or `.png` format, **Deed of Incorporation** (Escrituras de Constitución) and active powers of attorney (Poderes vigentes) registered with the Mercantile Registry, and recent **Tax Filings** (VAT return Modelo 303/390 or Corporate Tax return Modelo 200, 220, 202, or 222).
*   *Registration Process*: Go to `bbva.es`, select the **"Autónomos y Empresas"** tab, click `[Hazte cliente]`, complete the online form, upload the required documentation, and sign the contract digitally using Autofirma and your digital certificate.

##### Business Account Management Pillars
Effective corporate accounting for companies with annual revenues exceeding €5 million relies on five core pillars:
1.  **Accurate Transaction Logging**: Real-time recording of all financial movements, including income, expenses, investments, assets, and liabilities.
2.  **Plan General Contable (PGC) Alignment**: Structuring accounts according to Spain's PGC framework:
    *   *Group 1*: Basic Financing (capital, reserves, long-term loans).
    *   *Group 2*: Non-Current Assets (land, buildings, machinery).
    *   *Group 3*: Inventories (raw materials, work-in-progress, merchandise).
    *   *Group 4*: Commercial Creditors and Debtors (clients, providers).
    *   *Group 5*: Financial Accounts (banks, cash, short-term investments).
    *   *Group 6*: Purchases and Expenses (goods consumed, external services, payroll).
    *   *Group 7*: Sales and Income (product sales, services rendered).
    *   *Group 8 & 9*: Equity adjustments and exceptional expenses/income.
3.  **Regular Reconciliation**: Conducting monthly, quarterly, and annual ledger closures to identify and correct discrepancies.
4.  **Regulatory Compliance**: Aligning accounting practices with current tax laws to prevent legal issues or financial penalties.
5.  **Audit Readiness**: Maintaining clear documentation and transaction histories to ensure full transparency for internal and external audits.

#### 5.2.4 Préstamo Rápido (Fast Track Loan)

The **Préstamo Rápido** is an online loan designed for new clients, offering financing between **€3,000 and €10,000**.

```
                                  [Préstamo Rápido Application]
                                                │
                       ┌────────────────────────┴────────────────────────┐
                       ▼                                                 ▼
               [No-Document Path]                                [Document Path]
         (Available on Web & App)                            (Available on Web & App)
                       │                                                 │
  1. Connect external bank account where              1. Input personal, contact, and
     payroll/pension is deposited.                       professional details.
                       │                                                 │
  2. BBVA securely analyzes transaction               2. Upload required documents:
     history (credentials are deleted).                  - NIF/DNI
                       │                                 - Recent payroll slip (or IRPF if self-employed)
  3. Decision delivered within 24 business hours.        - Vida Laboral (employment history)
                       │                                 - Proof of external account number
  4. Sign contract online using DNI.                                     │
                       │                              3. Documents verified by BBVA.
  5. Choose payout destination:                                          │
     - BBVA Account: Immediate payout                 4. Sign contract (sent via email,
     - External Account: ~72 hours                       physical copy collected by courier).
                                                                         │
                                                      5. Choose payout destination:
                                                         - BBVA Account: Immediate payout
                                                         - External Account: ~72 hours
```

#### 5.2.5 Online Account for Minors (Children's Account)

The **Online Account for Minors** is a fee-free account designed for children and teenagers, managed under parental or guardian supervision.

##### Age Groups & Features
*   **Under 12 Years Old (Ages 0–11)**: Designed to receive direct deposits for scholarships, grants, or family savings. Features a **Fee-Free Online Account** with €0 administration and maintenance fees (0% NIR / 0% APR).
*   **Teenagers (Ages 12–17)**: Includes a **Fee-Free Online Account**, a linked **Goals Savings Account**, **Bizum for Minors** (with parental-controlled transaction limits), a **Free Aqua Debit Card** (no issuance or maintenance fees), a **Free Travel Pack** (fee-free transactions and cash withdrawals abroad), and a simplified version of the BBVA App.

##### Parental Controls & Security
Parents or guardians retain full control over the minor's account through their own BBVA App:
*   *Spending Limits*: Set custom daily or monthly spending limits on the minor's debit card.
*   *Card Control*: Instantly lock or unlock the card via the app.
*   *Real-Time Alerts*: Receive instant notifications for all card transactions, Bizum transfers, and ATM withdrawals.
*   *Merchant Blocking*: Transactions are automatically blocked in restricted categories, such as online gaming, casinos, and gambling sites.
*   *Fund Management*: Parents can transfer allowances directly to the minor's account and manage the linked Goals Savings Account, which is restricted from direct withdrawals by the minor.

##### International Card Usage (Aqua Debit Card)
The minor's Aqua Debit Card is optimized for international travel, such as study exchanges:
*   *Purchases in Foreign Currencies*: At the merchant's POS terminal, select payment in the local currency (e.g., USD). The transaction is processed using the standard exchange rate applied by the card network (Visa/Mastercard). BBVA automatically refunds the currency exchange fee once the transaction is finalized.
*   *ATM Withdrawals Abroad*: The minor can withdraw cash in a foreign currency up to **3 times per month** at any international ATM. If the ATM prompts to apply its own exchange rate, select **"No"** to allow BBVA to handle the conversion. The transaction will initially incur the card network's exchange fee and BBVA's international withdrawal fee. BBVA automatically refunds both fees once the transaction is finalized. *Note: Any direct fees charged by the ATM operator itself cannot be refunded by BBVA.*

##### Step-by-Step Opening Process

###### Scenario A: Parent is not a BBVA Client (Opening two accounts)
1. Go to `bbva.es` or the BBVA App and select **"Open account"**.
2. Complete the registration to open your own **Fee-Free Online Account**, verifying your identity with photos of your DNI/TIE.
3. Once your account is set up, proceed with the application for the **Online Account for Children**.
4. Upload photos of the child's DNI/TIE and the **Family Book** (Libro de Familia) or birth certificate to prove relationship.
5. Complete a verification video call with a BBVA representative (or complete the process in-app without a call if prompted). Both accounts will be activated within minutes.

###### Scenario B: Parent is an Existing BBVA Client (Opening minor account only)
1. Log into the BBVA App.
2. Go to the bottom menu, tap `[Contratar]` > `[Cuentas]` > `[Online Account for Minors]` (or navigate to the same path in your private area on `bbva.es`).
3. Complete the application steps.
4. Upload photos of the child's DNI/TIE and the **Family Book** or birth certificate.
5. Once verified, the account is activated.

##### Managing Account Visibility
By default, the minor's account is hidden in the parent's online profile. To make it visible:
1. Open the main menu in the BBVA App and select `[Configuración]`.
2. Tap **"Configure products"**.
3. Locate the minor's account and toggle the setting to **"Visible"** (view only) or **"Visible and operational"** (view and perform transactions).

##### Transition at Age 18
When the minor turns 18, the account transitions to a standard adult account:
*   The account remains fee-free and is transferred fully into the individual's name.
*   Parental/guardian representation is automatically removed.
*   To complete the transition, the account holder must verify their identity via a video call or video selfie in the BBVA App to gain full access to adult banking features.