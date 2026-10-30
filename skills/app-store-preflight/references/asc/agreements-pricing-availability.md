# App Store Connect: Agreements, Tax, Banking, Pricing, Availability, Distribution and Account Compliance
Source: https://developer.apple.com/help/app-store-connect/  
Retrieved: 2026-10-30

## BIZ.1 Sign and update agreements

**Source page:** https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements

**Source text (verbatim):**
> By joining the Apple Developer Program, you can distribute free apps on the App Store under the Apple Developer Program License Agreement.
>
> To sell your apps on the App Store or offer In-App Purchases, the Account Holder must sign the Paid Apps Agreement.
>
> Required role: Account Holder. View role permissions.

**Applies to:** All apps

- **[BIZ-01]** If the app is sold for a price or offers In-App Purchases, has the Account Holder signed the Paid Apps Agreement?
  - quote: "To sell your apps on the App Store or offer In-App Purchases, the Account Holder must sign the Paid Apps Agreement."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab: the Paid Apps row exists and is signed. Determine whether the app is paid (Pricing and Availability > Price Schedule) or uses In-App Purchases (In-App Purchases/Subscriptions sections in App Store Connect; in the Xcode project search for StoreKit usage such as Product.products, product.purchase, SKPaymentQueue, or a .storekit configuration file).
  - fix: Account Holder: Business > Agreements > Paid Apps row > View and Agree to Terms, then Agree. Otherwise offer the app for free with no In-App Purchases.

## BIZ.2 Sign a paid agreement

**Source page:** https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements

**Source text (verbatim):**
> - Select Business at the top of the page.
> - On the Agreements tab, find the Paid Apps row, then click View and Agree to Terms.
>
> You may be prompted to provide a two-factor authentication verification code in order to proceed. Learn how to get a verification code.
>
> - Read and accept the terms, then click Agree. You can also download a copy of the agreement.
>
> Important: Once you've accepted the terms of this agreement, you can’t undo this action.

**Applies to:** Developers who sell apps or offer In-App Purchases

## BIZ.3 Renew an expiring Paid Apps Agreement

**Source page:** https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements

**Source text (verbatim):**
> If you renew your membership after it expires, you’ll need to agree to the Paid Apps Agreement again. This agreement must be active in order for you to submit or update paid apps and In-App Purchases.
>
> - Select Business at the top of the page.
> - On the Agreements tab, find the Paid Apps row, then click Renew Agreement.

**Applies to:** Developers with paid apps or In-App Purchases whose membership expired and was renewed

- **[BIZ-02]** For a paid app or an app with In-App Purchases, is the Paid Apps Agreement active (not expired) at the time of submission?
  - quote: "This agreement must be active in order for you to submit or update paid apps and In-App Purchases."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab: Paid Apps row status. If membership was renewed after expiry, look for a Renew Agreement button on the Paid Apps row.
  - fix: Account Holder: Business > Agreements > Paid Apps row > Renew Agreement (or View and Agree to Terms).

## BIZ.4 Accept the latest agreement

**Source page:** https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements

**Source text (verbatim):**
> When a new version of the Paid Apps Agreement is available for you to sign, an alert appears in App Store Connect. You won’t be able to create a new app or In-App Purchase until you’ve agreed to the most recent version of the Paid Apps Agreement.
>
> - Select Business at the top of the page.
> - On the Agreements tab, find the Paid Apps row, then click View and Agree to Terms.
> - In the dialog, read and accept the terms, then click Submit.

**Applies to:** Developers with a Paid Apps Agreement

- **[BIZ-03]** Has the most recent version of the Paid Apps Agreement been agreed to (required before a new app or In-App Purchase can be created)?
  - quote: "You won’t be able to create a new app or In-App Purchase until you’ve agreed to the most recent version of the Paid Apps Agreement."
  - surface: asc
  - verify: App Store Connect: check for an agreement alert banner; Business > Agreements tab: Paid Apps row status is not Active (New Agreement Available) or Pending (New Agreement Available).
  - fix: Account Holder: Business > Agreements > Paid Apps row > View and Agree to Terms, accept the terms, click Submit.

## BIZ.5 Update your legal entity information or address

**Source page:** https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements

**Source text (verbatim):**
> Legal entity information is provided when enrolling in the Apple Developer Program and is tied to contracts associated with your membership.
>
> To update the legal entity name and address that appear in Business, contact us.
>
> Keep in mind that:
>
> - You may need to provide business documentation to support your request.
> - Once changes are approved, it can take up to two weeks for the updates to appear in App Store Connect.
>
> Provide any updated tax or banking information. Some updates may generate a new Paid Apps Agreement, which you can accept after the update finishes processing. The App Store will display your new legal entity name.

**Applies to:** Developers changing the legal entity name or address

- **[BIZ-04]** After a legal entity name or address change, has updated tax and banking information been provided and any newly generated Paid Apps Agreement been accepted?
  - quote: "Some updates may generate a new Paid Apps Agreement, which you can accept after the update finishes processing."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab: Paid Apps status is not Pending (New Legal Entity) or Pending (Update Legal Entity); Tax Forms and Bank Accounts sections reflect the new legal entity.
  - fix: Provide the updated tax and banking information; the Account Holder accepts the new Paid Apps Agreement once processing finishes.

## BIZ.6 View agreements status

**Source page:** https://developer.apple.com/help/app-store-connect/manage-agreements/view-agreements-status

**Source text (verbatim):**
> You can view Paid Applications Agreement’s terms, statuses, and expiration dates, as well as enter missing information and download PDF copies.
>
> Note: View and download the Free Apps Agreement, also known as the Apple Developer Program License Agreement, in Agreements and Guidelines for Apple Developers. You can also download it from the Membership section of your developer account by clicking Show Agreements.
>
> Required role: Account Holder, Admin, or Finance. View role permissions.

**Applies to:** All apps

## BIZ.7 View the status of an agreement

**Source page:** https://developer.apple.com/help/app-store-connect/manage-agreements/view-agreements-status

**Source text (verbatim):**
> The agreement status indicates whether your agreement is active or if it needs your attention.
>
> - Select Business at the top of the page.
> - On the Agreements tab, find the agreement you want to view. The status appears in the corresponding row.
>
> | Status | Description |
> |---|---|
> | New | The agreement hasn't been signed. |
> | Pending User Info | You’ve signed an agreement, but it’s not in effect because you haven’t finished providing required information. |
> | Processing | You’ve provided all the information and we’re reviewing your agreement. |
> | Verifying | You’ve provided additional information about the legal entity associated with the agreement and the details are being reviewed. |
> | Active | The agreement is in effect. |
> | Active (Pending User) | The agreement is in effect, but you haven’t finished providing required information. |
> | Active (New Agreement Available) | A new version of the existing active agreement is available for you to sign. |
> | Pending (New Legal Entity) | You’ve made changes to your legal entity and you're required to sign a new contract using the updated legal entity. |
> | Pending (Update Legal Entity) | You’ve made changes to your legal entity and new banking and/or tax forms are required. |
> | Pending (New Agreement Available) | A new version of the existing pending agreement is available for you to sign. |
> | Expired | The agreement has expired. |
> | Disabled | The Agreement is disabled, and your app is removed from the App Store until you provide the required information and the information is accepted by Apple. |

**Applies to:** Developers with a Paid Applications Agreement

- **[BIZ-05]** For a paid app or an app with In-App Purchases, is the Paid Apps Agreement in effect (status not New, Pending User Info, Processing, Verifying, Expired, or a Pending (...) status)?
  - quote: "You’ve signed an agreement, but it’s not in effect because you haven’t finished providing required information."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab: read the status in the Paid Apps row and compare against the status table.
  - fix: Complete whatever the status calls for: sign (New), finish required tax/banking information (Pending User Info, Active (Pending User)), sign the new version (New Agreement Available), or wait for review (Processing, Verifying).
- **[BIZ-06]** Is the agreement not in Disabled status?
  - quote: "The Agreement is disabled, and your app is removed from the App Store until you provide the required information and the information is accepted by Apple."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab: Paid Apps row status.
  - fix: Provide the required information indicated in Business until Apple accepts it.

## BIZ.8 Download a copy of an agreement

**Source page:** https://developer.apple.com/help/app-store-connect/manage-agreements/view-agreements-status

**Source text (verbatim):**
> You can download a copy of your agreements at any time in App Store Connect.
>
> - Select Business at the top of the page.
> - On the Agreements tab, click the agreement you want to download.
>
> Note:  You can also click the download icon to the right of the agreement to download.
>
> - Click Download at the top right corner of the prompt.

**Applies to:** All apps

## BIZ.9 Enter banking information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information

**Source text (verbatim):**
> To receive payments from Apple, you need to submit electronic banking information. Note that in order to add banking information, you’ll first need to sign a Paid Apps Agreement.
>
> Provide information specific to your bank (not an intermediary or correspondent bank) and ensure the routing number is unique to your account.
>
> In certain regions, additional documentation may be required to receive payments. If an Apple banking partner needs more documentation than what you provided, they’ll reach out to you directly. To verify a request before responding, contact us. Apple may also request additional information.
>
> You must submit all required tax forms needed for your paid contract in order for us to process banking information.
>
> Required role: Account Holder, Admin, or Finance. View role permissions.

**Applies to:** Developers receiving payments from Apple (requires a signed Paid Apps Agreement)

- **[BIZ-07]** If the app is paid or offers In-App Purchases, has electronic banking information been submitted (needed to receive payments from Apple)?
  - quote: "To receive payments from Apple, you need to submit electronic banking information."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab > Bank Accounts section shows a bank account (not empty, not Pending).
  - fix: Account Holder, Admin, or Finance: Business > Agreements > Bank Accounts > Add Bank Account.
- **[BIZ-08]** Have all required tax forms for the paid contract been submitted so the banking information can be processed?
  - quote: "You must submit all required tax forms needed for your paid contract in order for us to process banking information."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab > Tax Forms section: every listed form is submitted.
  - fix: Complete the outstanding tax forms (Business > Agreements > Tax Forms > Add Tax Info).
- **[BIZ-53]** Is the banking information for the developer's own bank (not an intermediary or correspondent bank), with a routing number unique to the account?
  - quote: "Provide information specific to your bank (not an intermediary or correspondent bank) and ensure the routing number is unique to your account."
  - surface: manual
  - verify: Compare App Store Connect > Business > Agreements > Bank Accounts > account details (bank, branch, routing number) against the bank's own records.
  - fix: Edit the bank information, or change the primary bank account if the bank code or account number must change.

## BIZ.10 Add banking information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information

**Source text (verbatim):**
> - Select Business at the top of the page.
> - On the Agreements tab, find the Bank Accounts section and click Add Bank Account. If you’ve already added another bank account and want to use new banking information, click the add button (+), then click Add New Account.
>
> You may be prompted to provide a two-factor authentication verification code in order to proceed. Learn how to get a verification code.
>
> - Select your bank country or region, then click Next.
> - Complete the required fields, then click Next.
> - In the Bank Account Currency pop-up menu, choose the primary currency of the bank account to ensure successful payments.
> - In the Account Type pop-up menu, select whether your bank account is Checking or Savings.
> - In the Account Name field, optionally enter a personal name for your bank.
> - Click “Don’t know your [local clearing code number]?” to search by your bank’s name, city, or postal code to find and select your bank. Not all branch locations are published in App Store Connect. Select a branch using the routing number for your bank account if your branch location isn’t listed.
> - In the Account Number field, enter the bank account number of the legal entity or individual enrolled in the Apple Developer Program.
> - In the IBAN field, enter your IBAN (International Bank Account Number) if applicable. An IBAN is used for payments to bank accounts in Europe and certain other regions.
> - Enter the details for the bank account holder, then click Next.
>
> Make sure to enter your information exactly as it appears on your bank account or your payment may be rejected.
>
> - Select the checkbox next to “I have read and agree to the statement above,” then click Add.
>
> If you hold the Admin or Finance role and are trying to add banking information, the Account Holder will need to approve the information in App Store Connect before it’s processed.
>
> Once your banking information is complete, it appears in the Bank Accounts section. Depending on where your bank is located, there may be additional required fields.

**Applies to:** Developers adding a bank account

- **[BIZ-09]** Do the bank account holder details match exactly what appears on the bank account?
  - quote: "Make sure to enter your information exactly as it appears on your bank account or your payment may be rejected."
  - surface: manual
  - verify: Compare App Store Connect > Business > Agreements > Bank Accounts > account details against the bank statement (account holder name, address, account number with leading zeros, IBAN in its own field).
  - fix: Edit the bank information (Business > Agreements > Bank Accounts > account name) to match the bank record.
- **[BIZ-54]** Is the Bank Account Currency set to the primary currency of the bank account?
  - quote: "In the Bank Account Currency pop-up menu, choose the primary currency of the bank account to ensure successful payments."
  - surface: manual
  - verify: App Store Connect > Business > Agreements > Bank Accounts > account details: Bank Account Currency matches the account's primary currency on the bank record.
  - fix: Edit the bank information and select the correct Bank Account Currency.
- **[BIZ-10]** If an Admin or Finance user added the banking information, has the Account Holder approved it?
  - quote: "If you hold the Admin or Finance role and are trying to add banking information, the Account Holder will need to approve the information in App Store Connect before it’s processed."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Bank Accounts: no row in Pending status.
  - fix: Account Holder: Business > Agreements > Bank Accounts > Review Changes > Approve.

## BIZ.11 Edit existing bank information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information

**Source text (verbatim):**
> You can update your banking information at any time. However, payment may not be sent to your new bank account until a future payment if changes are made after payment processing has begun for the fiscal month.
>
> - Select Business at the top of the page.
> - To edit your primary bank account, click the name of the account on the Agreements tab under Bank Accounts
>
> If you’ve added more than one bank account and want to edit another account, click Manage on the Agreements tab next to Bank Accounts, then click the name of the account you want to edit.
>
> You may be prompted to provide a two-factor authentication verification code in order to proceed. Learn how to get a verification code.
>
> - Make your edits, then select the checkbox next to “I have read and agreed to the statement above.”
> - Click Save.

**Applies to:** Developers editing a bank account

## BIZ.12 Remove bank information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information

**Source text (verbatim):**
> You can remove a bank account if it has the Not In Use status. To remove the banking information associated with your primary bank account, you must first change your primary bank account to a new or other existing bank account.
>
> - Select Business at the top of the page.
> - On the Agreements tab, under Bank Accounts, click Manage.
> - Click Remove, then click Remove again to confirm.

**Applies to:** Developers removing a bank account

## BIZ.13 Change your primary bank account

**Source page:** https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information

**Source text (verbatim):**
> You can update your banking information at any time. However, changes made after payment processing has begun for the fiscal month will delay the switch to your new bank account until the next payment cycle.
>
> - Select Business at the top of the page.
> - On the Agreements tab, click the add button (+) in the Bank Accounts section.
> - In the pop-up menu, choose Add New Account or Add from Existing Accounts.
>
> If you'd like to change your primary bank account to a previously used account, choose Add from Existing Accounts and pick the desired bank from the list provided.
>
> If you'd like to change your primary bank account to a a new bank account, choose Add New Account and enter new banking information details as described in details in the Adding Banking Information section.
>
> - You may be prompted to provide a two-factor authentication verification code in order to proceed. Learn how to get a verification code.
> - If you hold the Admin or Finance role and are choosing Add New Account, the Account Holder will need to approve the new banking information in App Store Connect before the change is processed.

**Applies to:** Developers changing the primary bank account

## BIZ.14 Approve a pending banking change

**Source page:** https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information

**Source text (verbatim):**
> If you’re the Account Holder for a team with multiple App Store Connect users, you'll need to approve the following banking information changes before they’re processed:
>
> - Adding a new bank account
> - Replacing a bank account
> - Editing an IBAN
>
> When an Admin or Finance user initiates a change, the Account Holder receives an email asking them to review the updated information in App Store Connect.
>
> - Select Business at the top of the page.
> - In the Agreements tab, under Bank Accounts, click Review Changes for the row with a Pending status. You’ll be shown the proposed change.
> - Click Approve to authorize the change or click Reject to deny the change.
> - You'll be asked to confirm your decision. If you’re approving a change, click Approve again to confirm your selection.
>
> After the Account Holder approves the change, it will be processed within 24 hours. If they reject the change or if it isn’t approved within 30 days, your bank account details will not be updated.
>
> | Property to edit | How to update |
> |---|---|
> | Account Holder Name<br>Address<br>Account Holder Type<br>Bank Account Type<br>Bank Account Currency<br>IBAN1 (if applicable), or other country- or region-specific information such as tax IDs or vendor contact information | Follow the steps in "Edit existing bank information." |
> | Bank Territory<br>Bank Code<br>Bank Account Number | Follow the steps in "Change your primary bank account." |
> | Select another bank account that's already set up | Follow the steps in "Change your primary bank account." |
>
> 1If you hold the Admin or Finance role and are updating the IBAN, the Account Holder will need to approve the change in App Store Connect before it’s processed.

**Applies to:** Account Holders of teams with multiple App Store Connect users

- **[BIZ-11]** Are there no banking changes left in Pending status awaiting Account Holder approval?
  - quote: "If they reject the change or if it isn’t approved within 30 days, your bank account details will not be updated."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Bank Accounts: look for a row with a Pending status and a Review Changes link.
  - fix: Account Holder: click Review Changes, then Approve (or Reject).

## BIZ.15 FAQs

**Source page:** https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information

**Source text (verbatim):**
> Can I receive payments to multiple banks?
>
> No. You may only receive payments at one bank.
>
> Why am I getting a “Please enter valid bank account number” error message?
>
> If your bank account number has leading zeros, make sure you’ve included all leading zeros when entering your banking information. Your bank account number and your IBAN are two separate numbers. Make sure you haven’t entered your IBAN in the bank account number field.

**Applies to:** All developers entering banking information

## BIZ.16 Provide tax information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> To receive payments from Apple, you'll also need to enter banking information and submit tax forms in accordance to local laws. App Store Connect will verify the information you provide.
>
> In order to submit tax forms, you first need to sign the Paid Apps Agreement. The required tax forms will display, many of which can be submitted electronically.
>
> All developers must complete a US tax form to comply with the Paid Apps Agreement. Depending on where your developer account is based, you may be required to submit additional tax forms. Review the list of countries below to understand any other requirements that may be applicable to you.
>
> US-based
>
> If you’re based in the United States, you’re prompted to complete a W-9 form. The US tax form section will display a field for a tax identification number.
>
> - For an individual, this is a Social Security Number (SSN), which is also an Individual Taxpayer Identification Number (ITIN).
> - For a business entity, the taxpayer identification number is the Employer Identification Number (EIN).
>
> Learn more about tax identification numbers.
>
> Non-US-based
>
> If you’re based outside the United States, the W-8BEN, W-8BEN-E, or W-8ECI may be required, but you'll be prompted to answer a series of questions to direct you to the most appropriate tax form and any applicable certification. If your tax form isn’t available to you in App Store Connect, contact us.
>
> Tip: Use the downloadable instructions and tip sheets near the top of the page to help you provide the right information for your W9, W-8BEN, or W-8BEN-E.
>
> Once you submit this information, you won’t be able to make any changes in App Store Connect. For any corrections or additional tax forms, contact us. Information you originally provided in App Store Connect may continue to display even after we have your updated information on file.
>
> Required role: Account Holder, Admin, or Finance. View role permissions.
>
> - Select Business at the top of the page.
> - On the Agreements tab, find the Tax Forms section.
> - Click Add Tax Info next the tax form you want to complete.
>
> If the tax form you want to complete isn’t appearing, click the (+) button next to Tax Forms, select Paid Apps from the menu, check the tax form you want to add, then click Add.
>
> The tax forms that display depend on where your developer account is based. Contact us if you need to make changes.
>
> - Enter the requested information.
> - Verify that the information you entered is correct and complete, then click Submit.
>
> Some tax forms can be modified in App Store Connect, but you'll need to contact us to update others. Changes will be reflected in the same month’s earnings if the update is made before the end of the fiscal month, otherwise your status will be updated for the following month’s earnings.

**Applies to:** Developers receiving payments from Apple (requires a signed Paid Apps Agreement)

- **[BIZ-12]** Has a US tax form (W-9, or W-8BEN / W-8BEN-E / W-8ECI as directed) been completed?
  - quote: "All developers must complete a US tax form to comply with the Paid Apps Agreement."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab > Tax Forms section: the US tax form shows as submitted.
  - fix: Account Holder, Admin, or Finance: Business > Agreements > Tax Forms > Add Tax Info and complete the US form.
- **[BIZ-13]** Have any additional tax forms required for the country or region where the developer account is based been submitted?
  - quote: "Depending on where your developer account is based, you may be required to submit additional tax forms."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: all forms displayed are submitted; check the country sections in this file for the account’s base country or region.
  - fix: Add the missing form via Tax Forms > Add Tax Info, or the (+) button next to Tax Forms > Paid Apps.
- **[BIZ-14]** Was the tax information verified as correct and complete before clicking Submit?
  - quote: "Once you submit this information, you won’t be able to make any changes in App Store Connect."
  - surface: manual
  - verify: Before submitting a tax form, review every field against official tax documents.
  - fix: If already submitted with errors, contact Apple (corrections cannot be made in App Store Connect).

## BIZ.17 Australia

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in Australia.
>
> Although you may not be required to register for Goods and Services Tax (GST) with the Australian government, Apple requires that Australia-based developers have a GST registration to sell apps.
>
> Required tax information:
>
> Australian Business Number (ABN) and proof of GST Registration.
>
> The evidence can be screenshots or PDF files of the ABN registration. Collect the current details with enough information to associate this ABN with the legal entity name you’ve given Apple and the historical details to show that the developer is registered for the GST.
>
> Edit tax information:
>
> Once you submit this information, you won’t be able to make any changes in App Store Connect. For any corrections or additional tax forms, contact us.
>
> Learn more about recipient-created tax invoices.

**Applies to:** Developers based in Australia

- **[BIZ-15]** Does the Australia-based developer have a GST registration and has the ABN with proof of GST registration been provided?
  - quote: "Apple requires that Australia-based developers have a GST registration to sell apps."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: Australia tax form submitted with ABN and proof of GST registration.
  - fix: Register for GST, then submit the ABN and proof of GST registration (screenshots or PDFs of the ABN registration) in Business > Agreements > Tax Forms.

## BIZ.18 Brazil

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in Brazil.
>
> Required tax information:
>
> Cadastro Nacional de Pessoas Jurídicas (CNPJ), a 14 character corporate tax ID.
>
> Optional tax information:
>
> If you’re based outside of Brazil and your country or region of residence has a tax treaty agreement with Brazil, you may also upload your tax residency certificate. If you don’t provide a certificate, your sales in Brazil may be subject to the applicable withholding tax at the standard rate. If your region is denied under the Brazilian legislation, no reduced rate of withholding is available. Contact your tax authority if you have questions regarding how to obtain a tax residency certificate.
>
> Your withholding tax rate won’t be reduced until your tax residency certificate is received and reviewed for applicable treaty benefits between Brazil and your country or region of residence. You can start selling content in Brazil (assuming you’ve submitted all required banking and tax information), but payments will be subject to the applicable withholding tax at the standard rate until your residency certificate is reviewed and tax rate benefits are confirmed.
>
> Edit tax information:
>
> You can update your Brazil tax registration status at any time in App Store Connect.
>
> Once you submit this information, you won’t be able to make any changes in App Store Connect. For any corrections or additional tax forms, contact us.
>
> Learn more about monthly withholding tax information.
>
> Learn more about annual withholding tax certificate.

**Applies to:** Developers based in Brazil

- **[BIZ-16]** Has the Brazil-based developer provided its CNPJ?
  - quote: "Cadastro Nacional de Pessoas Jurídicas (CNPJ), a 14 character corporate tax ID."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: Brazil tax form submitted with a 14-character CNPJ.
  - fix: Complete the Brazil tax form in Business > Agreements > Tax Forms.

## BIZ.19 Canada

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in Canada.
>
> Required tax information:
>
> If you’re based in Canada, you’re required to submit your Canadian Goods and Services tax (GST)/Harmonized Sales Tax (HST) number (and Québec Sales Tax (QST) number if based in Quebec).
>
> In accordance with Canadian law, your remittances for sales on the App Store in Canada will be reduced by the applicable Canadian GST/HST and QST/PST on Apple’s commission. This reduction for GST/HST & QST/PST results in a tax paid by you and a tax credit for GST/HST and/or QST may be available as allowed under Canadian Tax Regulations. Apple will issue you a tax on commission invoice on a monthly basis, available in App Store Connect.
>
> Your certification will populate Part 4 of the Quebec Form FP-2506-V, or part D of GST/HST Form 506. Apple will complete Part 5 or Part E respectively, and make the form available for you to download for your records.
>
> Optional tax information:
>
> If you’re based outside of Canada, you may send either or both of the following forms to Apple:
>
> - GST506 (if registered for GST)
> - Quebec Form FP 2506-V (if registered for QST)
>
> They can be emailed to canada_tax@apple.com (preferred) or mailed to:
>
> Apple Canada Inc.
>
> MS: 580-GL
>
> 12545 Riata Vista Circle
>
> Austin, TX 78727-6524
>
> USA
>
> Edit tax information:
>
> If you’re based in Canada, you can update your Canada tax information at any time in App Store Connect.
>
> If you’re based outside of Canada and need to send updated Canada tax forms for processing, they can be emailed to canada_tax@apple.com or contact us.
>
> Learn more about tax on commission invoices.

**Applies to:** Developers based in Canada

- **[BIZ-17]** Has the Canada-based developer submitted its GST/HST number (and QST number if based in Quebec)?
  - quote: "If you’re based in Canada, you’re required to submit your Canadian Goods and Services tax (GST)/Harmonized Sales Tax (HST) number (and Québec Sales Tax (QST) number if based in Quebec)."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: Canada tax form submitted with GST/HST (and QST) number.
  - fix: Complete the Canada tax form in Business > Agreements > Tax Forms.

## BIZ.20 Ireland

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in Ireland and registered for VAT in Ireland.
>
> Required tax information:
>
> An Irish Value Added Tax (VAT) Identification Number.
>
> Edit tax information:
>
> You can update your Ireland tax registration status at any time in App Store Connect.
>
> Timely completing and updating Ireland tax forms in App Store Connect is required to ensure your proceeds are calculated correctly. Failure to provide these details will result in Apple not paying you any Irish VAT you may owe to Revenue Commissioners.
>
> Learn more about Ireland self-billing invoices.

**Applies to:** Developers based in Ireland and registered for VAT in Ireland

- **[BIZ-18]** If the developer is based in Ireland and registered for VAT in Ireland, has the Irish VAT Identification Number been provided?
  - quote: "An Irish Value Added Tax (VAT) Identification Number."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: Ireland tax form submitted.
  - fix: Complete the Ireland tax form in Business > Agreements > Tax Forms.

## BIZ.21 Mexico

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in Mexico or registered for tax in Mexico.
>
> All sales on the App Store in Mexico are subject to a Value-Added Tax (VAT).
>
> Apple will collect and remit the VAT directly to the tax authority in Mexico for:
>
> - Non-tax registered individuals based in Mexico or outside of Mexico
> - Non-tax registered companies based outside of Mexico
>
> Apple will collect and remit the VAT to you if you're:
>
> - Tax-registered individuals based in Mexico or outside of Mexico
> - Tax-registered companies based outside of Mexico
> - All companies based in Mexico
>
> You’ll then need to remit the VAT in the appropriate manner to the tax authority in Mexico and submit tax information to Apple.
>
> Required tax information:
>
> If you’re based in Mexico, a withholding income tax and VAT on Apple’s commission may also apply, as described below. Where applicable, a VAT invoice on Apple’s commission and withholding income tax statement will be issued on a monthly basis.
>
> Companies:
>
> - Clave en el RFC
> - Cédula de Identificación Fiscal.
>
> Your earnings will be reduced based on the VAT on Apple’s commission, for which you may be able to receive an input tax credit.
>
> Tax-registered individuals:
>
> - Clave en el RFC
> - Clave Única de Registro de Población
> - Cédula de Identificación Fiscal.
>
> Your earnings will be reduced by the VAT on Apple’s commission, for which you may be able to receive an input tax credit, and withholding income tax on your total monthly worldwide sales before VAT.
>
> Non-tax-registered individuals:
>
> Your earnings will be reduced by the VAT on Apple’s commission, for which you may be able to receive an input tax credit, and withholding income tax on your total monthly worldwide sales before VAT.
>
> Edit tax information:
>
> You can update your Mexico tax information at any time in App Store Connect. Your changes will be reflected in the same month’s earnings if the update is made before the end of the fiscal month, otherwise your status will be updated for the following month’s earnings.
>
> Note: Apple’s fiscal month may not align exactly with the calendar month.
>
> Learn more about tax on commission invoices.
>
> Learn more about monthly withholding tax information.

**Applies to:** Developers based in Mexico or registered for tax in Mexico

- **[BIZ-19]** Has the required Mexico tax information been submitted to Apple?
  - quote: "You’ll then need to remit the VAT in the appropriate manner to the tax authority in Mexico and submit tax information to Apple."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: Mexico tax form submitted with the items listed for companies or tax-registered individuals.
  - fix: manual — requires developer decision/legal/business action

## BIZ.22 Singapore

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in Singapore.
>
> Required tax information:
>
> Singapore Goods and Services Tax (GST) registration number, or indicate a non-registered status for Singapore GST.
>
> A Singapore GST registration number is a 10-digit alphanumeric value issued by the IRAS. Consult with your tax advisor for information on the registration status appropriate for your business or organization.
>
> If you're a Singapore GST-registered developer, Apple’s commission earned in Korea (region code: KR) and South Asia and Pacific (region code: AP) in relation to your sales on apps and In-App Purchases on the App Store will be considered taxable.
>
> If you don't provide a Singapore GST registration number or indicate non-registered status, Apple’s worldwide commissions earned in relation to your sales on apps and In-App Purchases on the App Store will be considered taxable under the Singapore GST Act.
>
> Edit tax information:
>
> You can update your Singapore tax registration status at any time in App Store Connect.
>
> Timely completing and updating Singapore tax forms in App Store Connect is required to ensure your proceeds are calculated correctly. Please note tax on Apple's commission earned from scenarios mentioned above won't be adjusted retrospectively.
>
> Learn more about tax on commission invoices.

**Applies to:** Developers based in Singapore

- **[BIZ-20]** Has a Singapore GST registration number been provided, or non-registered status indicated?
  - quote: "Singapore Goods and Services Tax (GST) registration number, or indicate a non-registered status for Singapore GST."
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: Singapore tax form submitted.
  - fix: Complete the Singapore tax form in Business > Agreements > Tax Forms.

## BIZ.23 South Korea

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in South Korea.
>
> Required tax information:
>
> - A valid Korean Business registration number (BRN, 사업자등록번호) and
> - Certificate of Business Registration (BRC, 영문 사업자등록증명) issued within the past 90 days with an English translation,
>
> or
>
> - A valid registration number with the Korean National NTS (국세청 고유번호) and
> - Certificate of Registration with the NTS (고유번호증) issued within the past 90 days with an English translation.
>
> A standard BRN is generally used for organizations in South Korea, and a registration number with NTS may be used for nonprofit organizations. Consult with your tax advisor for information on the registration type appropriate for your business or organization.
>
> Failure to provide an up to date tax information may result in a delay of payment on your earnings and not receiving e-Tax invoices. In this scenario, cash receipts will be issued in lieu of e-Tax invoices. Learn more.
>
> Edit tax information:
>
> You can update your South Korea tax information in App Store Connect if it isn’t pending validation results.
>
> If you submit an updated BRN (사업자등록번호), an updated copy of the BRC (영문 사업자등록증명) issued within the past 90 days with an English translation will be required.
>
> If you submit an updated Registration with the NTS (국세청 고유번호), an updated copy of the Certificate of Registration with the NTS (고유번호증) issued within the past 90 days with an English translation will be required.
>
> Additionally, a banner will appear on the Agreements page if there is any missing tax information that is required. If you have any questions or concerns related to our verification results, please contact us.

**Applies to:** Developers based in South Korea

- **[BIZ-21]** Has a valid BRN (or NTS registration number) been provided together with its certificate issued within the past 90 days with an English translation?
  - quote: "issued within the past 90 days with an English translation"
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: South Korea tax form submitted; no banner on the Agreements page about missing required tax information.
  - fix: Upload the BRN and BRC (or NTS number and Certificate of Registration) issued within the past 90 days with an English translation.

## BIZ.24 Taiwan

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in Taiwan or developers that have a Taiwan Tax Identification Number (TIN).
>
> If you don’t file taxes in Taiwan, Taiwanese tax forms aren’t required. Apple collects and remits taxes to the appropriate tax authorities in Taiwan, consistent with Schedule 2 of the Paid Apps Agreement.
>
> Required tax information:
>
> Taiwan Tax Identification Number (TIN)
>
> The amount of tax collected will differ depending on whether you have provided a TIN in App Store Connect. Your TIN is necessary to ensure that we’re calculating your proceeds correctly.
>
> Edit tax information:
>
> Once you submit this page, you won’t be able to make any changes in App Store Connect. For any corrections or additional tax forms, contact us.

**Applies to:** Developers based in Taiwan or developers that have a Taiwan Tax Identification Number (TIN)

- **[BIZ-22]** If the developer files taxes in Taiwan, has the Taiwan TIN been provided?
  - quote: "Taiwan Tax Identification Number (TIN)"
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: Taiwan tax form submitted with TIN.
  - fix: Complete the Taiwan tax form in Business > Agreements > Tax Forms.

## BIZ.25 Thailand

**Source page:** https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information

**Source text (verbatim):**
> Tax forms required for:
>
> Developers based in Thailand.
>
> Required tax information:
>
> Thailand VAT registration number or indicate non-registered status
>
> If you don't provide a Thailand VAT registration number or indicate non-registered status, Apple’s commissions earned in relation to your sales on apps and In-App Purchases on the App Store in Thailand will be considered taxable under the Thailand tax regulations. Completing Thailand tax forms in App Store Connect are required to ensure your proceeds are calculated correctly.
>
> Edit tax information:
>
> You can update your Thailand tax information at any time in App Store Connect.
>
> Learn more about tax on commission invoices.

**Applies to:** Developers based in Thailand

- **[BIZ-23]** Has a Thailand VAT registration number been provided, or non-registered status indicated?
  - quote: "Thailand VAT registration number or indicate non-registered status"
  - surface: asc
  - verify: App Store Connect > Business > Agreements > Tax Forms: Thailand tax form submitted.
  - fix: Complete the Thailand tax form in Business > Agreements > Tax Forms.

## BIZ.26 Set a tax category

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-information/set-a-tax-category

**Source text (verbatim):**
> Apple's tax calculation service uses multiple inputs to compute tax on customer transactions in countries or regions where taxes are administered. These inputs include your tax category selection in App Store Connect, app metadata, legal entity status, tax registration status, customer attributes, and other requirements in accordance with local laws and regulations.
>
> You need to choose the category that most accurately describes each app. By default, this category applies to In-App Purchases. However, you also have the option to set a specific category for each In-App Purchase. If you modify any tax category settings, it will only impact future transactions.
>
> If you choose not to make any changes, your apps and In-App Purchases will be assigned the App Store software category. You can adjust these settings at any time as the characterization of your app or In-App Purchases change or as tax legislation changes. Ensure that the tax category settings you choose accurately represent your app's offerings. Selecting categories or attributes that aren't appropriate for your app or In-App Purchases violates your obligations under the Apple Developer Program License Agreement, the Paid Agreements, and local tax laws.
>
> Your tax category selections may result in changes to your proceeds, as proceeds are calculated based on the price of your app or In-App Purchase, minus any applicable taxes. To view your estimated proceeds at each price tier, click All Prices and Currencies from Pricing and Availability.
>
> Note:  Changes may take up to an hour to be reflected.
>
> Compare the categories below to determine which best describes your app and/or In-App Purchases. For guidance on setting the appropriate tax category, consult your tax advisor.
>
> | Category | Description |
> |---|---|
> | App Store software | If the primary purpose of your app isn't described by any of the categories below, keep your tax category set to App Store software. |
> | Artwork | Apps that sell digital artwork, including original or manipulated graphics, fonts, and images. If your app provides tools to create or edit artwork, keep your tax category set to "App Store software.” If your app sells photographic images, select the "Photography" category. |
> | Audiobooks | Apps that allow users to listen to audio versions of books. If your app contains episodic series of audio content, select the "Music and other audio" category. |
> | Books | Apps that sell electronic versions of printed books, or digital-only content that's published once, under a single title. For content published regularly, consider the "Magazines and other periodicals" category, or the "News publications" category. |
> | Boosting | Apps and/or In-App Purchases that offer resources to provide exposure, visibility, or engagement to enhance the prominence and reach of specific content that’s experienced or consumed in app (such as videos, sales of “boosts” in social media apps, listings, and/or other forms of user-generated content). |
> | Cloud media player | Apps that stream audio or visual content through the cloud. |
> | Cloud storage | Apps that store data in remote servers that can be accessed through the cloud. |
> | Dating | Apps that facilitate forming new interpersonal relationships by means of text, voice, photo, or video sharing. |
> | Fitness and health | Apps that provide streaming fitness classes or focus on healthy living. |
> | Games | Apps that provide single or multiplayer interactive activities for entertainment purposes. |
> | Greeting cards | Apps that create and send electronic versions of a decorative card to express good wishes for an occasion. |
> | Magazines and other periodicals | Apps that deliver content using an issue-based strategy or are producing interactive versions of a printed periodical. If your app contains news content, consider selecting the "News publications" category. |
> | Music and other audio | Apps that are for listening to audio content, including music, podcasts, meditations, radio, and ringtones. |
> | News publications | Apps that provide information about current events with regular content updates. It may be a digital-first, or interactive version of a printed newspaper. If your app focuses on content about one sector, consider the "Magazines and other periodicals" category. |
> | Photography | Apps that sell photos or assist in capturing, editing, managing, or sharing photos. |
> | Software training material | Apps that deliver trainings on specific off-the-shelf software. |
> | Video | Apps that stream video content. It may be accessed through a subscription, pay-per-view, or purchase for permanent consumption. |
>
> The first full month after you configure your settings, you can view taxes for US and Canadian transactions in the transaction tax report in Payments and Financial Reports. This report shows transaction taxes—such as sales tax, use tax, goods and services tax, and other similar taxes—applied to your sales and will be available no later than the second Friday of the fiscal month.
>
> Required role: Admin or App Manager. View role permissions.
>
> - In Apps, select your app. The page opens with the Distribution tab selected.
> - In the sidebar, click Pricing and Availability.
> - Next to Tax Category, click Edit.
> - In the dialog that appears, select the tax category that best describes your app.
>
> Depending on your selection, you may be asked to describe your app further by selecting either a subcategory or attributes or both.
>
> - Click Done.

**Applies to:** All apps

- **[BIZ-24]** Is the app’s tax category set to the category that most accurately describes the app (App Store software unless another category fits)?
  - quote: "You need to choose the category that most accurately describes each app."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Pricing and Availability > Tax Category; compare to what the app sells (e.g., Games, Video, Books, Audiobooks, News publications) using the category table.
  - fix: Pricing and Availability > Tax Category > Edit, select the best-fitting category (and subcategory/attributes if asked), click Done. Consult a tax advisor if unsure.

## BIZ.27 Set a price

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price

**Source text (verbatim):**
> In order to offer paid content on the App Store, your membership Account Holder will need to accept the Paid Apps Agreement in the Tax and Banking section of App Store Connect. If the most recent version of this agreement hasn’t been accepted, you can only offer your app for free.
>
> You’ll need to set pricing for your app before you submit it for review. Choose from up to 800 price points by default, and request to access an additional 100 higher price points (up to $10,000).
>
> You can set a price for the country or region you’re familiar with as the basis for automatically generating prices across the other 174 storefronts and 43 currencies. Automatically generated prices account for foreign exchange rates and certain taxes, and follow the most common pricing convention for each country or region.
>
> Periodically, Apple updates prices in certain regions based on changes in taxes and foreign exchange rates. This is done using publicly available exchange rate information from financial data providers. These automatic price adjustments help ensure that your app’s price across all storefronts stays equalized with your base country or region. Automatic price updates help your global earnings stay consistent, customers aren’t incentivized to seek lower prices on certain storefronts, and pricing mistakes are reduced. Apple will never change the price in your base country or region, and will always notify you in advance of changes on other storefronts.
>
> Alternatively, you can choose to manually manage certain storefronts or you can manually manage them all. Keep in mind that you'll be responsible for staying up to date with taxes and exchange rates in the storefronts you manually manage.
>
> You can set a price for your app using the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** All apps

- **[BIZ-25]** Has pricing been set for the app before submitting it for review?
  - quote: "You’ll need to set pricing for your app before you submit it for review."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Monetization > Pricing and Availability > Price Schedule shows a base country or region and a price (not just the Add Pricing button).
  - fix: Pricing and Availability > Price Schedule > Add Pricing; select base country or region and a price (Free or a price point), confirm.
- **[BIZ-26]** If the app has a price other than free, has the most recent Paid Apps Agreement been accepted?
  - quote: "If the most recent version of this agreement hasn’t been accepted, you can only offer your app for free."
  - surface: asc
  - verify: Compare Pricing and Availability > Price Schedule with Business > Agreements > Paid Apps status.
  - fix: Account Holder accepts the latest Paid Apps Agreement, or set the price to free.

## BIZ.28 Set a price for your app

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Pricing and Availability.
> - In the Price Schedule section, click Add Pricing.
> - Select a base country or region. Apple uses this base to provide comparable prices on the other 174 storefronts. Prices for your base country or region won’t be adjusted by Apple as taxes and foreign exchange rates change. You can change this base configuration later at any time.
> - Select a price for your base country or region, then click Next. Initially, the list displays 25 price points that follow the most common pricing convention for each country or region. To view more price points, scroll to the end of the menu and click See Additional Prices. You can choose from up to 800 price points by default. You can also submit a request to access an additional 100 higher price points.
> - A screen appears with comparable prices for all other storefronts. If you’d like Apple to automatically adjust prices for you, don’t make any changes to this pricing. Alternatively, you can choose different prices for individual countries or regions. If you select your own prices, Apple won’t adjust your pricing on those storefronts in the future.
> - Click Next.
> - Review your upcoming price, then click Confirm.

**Applies to:** All apps

## BIZ.29 Edit your app’s base country or region

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price

**Source text (verbatim):**
> When you update your app’s base country or region, its associated In-App Purchases automatically inherit its base country or region (unless you already edited their pricing or base country or region separately). The resulting price update for your app goes into effect immediately.
>
> - In Apps, select the app you want to review.
> - In the sidebar, under Monetization, click Pricing and Availability.
> - In the Price Schedule section under Base Country or Region, click Edit.
> - Changing your base country or region deletes any scheduled price changes. Review any scheduled price changes, select the box indicating you understand they’ll be permanently deleted, and click Edit.
> - Select a base country or region. Apple uses this as the base to provide comparable prices on the other 174 storefronts. As taxes and foreign exchange rates change, prices on the other storefronts will be automatically updated by Apple periodically. You can change this base configuration later at any time.
> - Select a price for your base country or region, then click Next. Initially, the list displays 25 price points that follow the most common pricing convention for each country or region. To view more price points, scroll to the end of the menu and click See Additional Prices. You can choose from up to 800 price points by default. You may also submit a request to access an additional 100 higher price points.
> - A screen appears with comparable prices for all other countries or regions based on taxes and foreign exchange rates. If you’d like Apple to automatically adjust prices for you, don’t make any changes to this pricing. Alternatively, you can choose different prices for individual countries or regions. If you select your own prices, Apple won’t adjust your pricing on those storefronts in the future.
> - Click Next.
> - Review your upcoming changes, then click Confirm.

**Applies to:** Apps changing their base country or region

## BIZ.30 Schedule price changes for apps

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/schedule-price-changes-for-apps

**Source text (verbatim):**
> If you’ve accepted the Paid Apps Agreement and submitted your app for review, you can schedule price changes for your app. Price changes can have definite start and end dates, or they can be permanent with no end. For example, you can set a promotional price for a month, then return to the regular price.
>
> | Property | Description |
> |---|---|
> | Global Price Change | You change the price of your app in your base country or region in App Store Connect. Apple provides comparable prices for all other countries or regions, and may adjust some prices on your behalf in the future to account for changes in taxes and foreign exchange rates. Pricing in your base country or region won't be affected. |
> | Temporary Price Change | You select the start and end dates for a temporary price change in certain countries or regions. During this time, Apple won’t adjust your prices in these countries or regions. |
> | Custom Price Change | You manually manage prices for some or all countries or regions. Apple won't adjust prices on your behalf in these countries or regions. |
>
> Learn how to schedule price changes for an app using the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** Apps whose developer has accepted the Paid Apps Agreement and submitted the app for review

## BIZ.31 Schedule a global price change

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/schedule-price-changes-for-apps

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Pricing and Availability.
> - Next to Price Schedule, click the add button (+).
> - Select Global Price Change, then click Next.
> - Select an effective date. Effective dates can be scheduled from today up to the end of the next calendar year.
> - Select a price for the base country or region. Apple uses this base to provide comparable prices on the other 174 storefronts. As taxes and foreign exchange rates change, prices on the other storefronts will be automatically updated by Apple periodically.
> - Review the prices for each country or region, then click Confirm.

**Applies to:** Apps scheduling a global price change

## BIZ.32 Schedule a temporary price change

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/schedule-price-changes-for-apps

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Pricing and Availability.
> - Next to Price Schedule, click the add button (+).
> - Select Temporary Price Change, then click Next.
> - Select start and end dates, then click Next. Start dates can be scheduled from today up to the end of the next calendar year. The longest length for a temporary price change is one year.
> - Select the App Store countries or regions where you'd like the price change to go into effect, then click Next.
> - Select a country or region and a price, then click Next. Apple will use this to provide comparable prices across the selected countries or regions.
> - Review the prices for each country or region. Make any necessary changes, then click Next.
>
> If your temporary price change includes your base country or region, note that Apple won’t make any automatic adjustments to your app’s pricing in all 175 countries or regions during the start and end dates you’ve selected. If you’d like to add more storefronts, click Back or Cancel. Otherwise, click Next.
>
> - Review your temporary price changes, then click Confirm.

**Applies to:** Apps scheduling a temporary price change

## BIZ.33 Schedule a custom price change (manually manage prices in specific countries or regions)

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/schedule-price-changes-for-apps

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Pricing and Availability.
> - Next to Price Schedule, click the add button (+).
> - Select Custom Price Change, then click Next.
> - Select an effective date. Effective dates can be scheduled from today up to the end of the next calendar year.
> - Choose the first option, “Manually manage prices in specific countries or regions”.
> - Select the countries or regions where you’d like to manually manage prices and click Next. You won’t be able to choose your base country or region.
> - Select a country or region and a price, then click Next. Apple will use this to provide comparable prices across the other storefronts you selected.
> - Review the prices for each country or region. Make any necessary changes, then click Next.
> - Review your upcoming changes, then click Confirm.
>
> Once the change goes into effect, Apple will no longer update your app’s pricing to account for changes in taxes or foreign exchange rates in the countries or regions you selected.

**Applies to:** Apps manually managing prices in specific countries or regions

## BIZ.34 Schedule a custom price change (manually manage prices in all 175 countries or regions)

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/schedule-price-changes-for-apps

**Source text (verbatim):**
> If you schedule a Custom Price Change that includes your base country or region in App Store Connect, Apple will no longer automatically update prices in any of the 175 App Store countries or regions.
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Pricing and Availability.
> - Next to Price Schedule, click the add button (+).
> - Select Custom Price Change, then click Next.
> - Select an effective date. Effective dates can be scheduled up to the end of the next calendar year.
> - Choose the second option, “Manually manage prices in all countries or regions”. Then, click Next.
> - Select a price for the base country or region. This price must be selected for you to manually manage prices in all 175 countries or regions, and you can keep the price as is or update it.
> - If you want to change prices in other countries or regions, select their prices. Countries or regions you don’t change will keep their existing prices.
> - Review the current prices for any countries or regions you didn’t select a price for, then click Next.
> - Review all of your upcoming changes and click Confirm.
>
> Once the change goes into effect, Apple won’t update pricing to account for changes in taxes or foreign exchange rates. If you do want Apple to automatically adjust prices for you, you need to create a global price change. Ensure you have read and understand the impact of Apple’s pricing capabilities.

**Applies to:** Apps manually managing prices in all countries or regions

## BIZ.35 View or edit upcoming price changes

**Source page:** https://developer.apple.com/help/app-store-connect/manage-app-pricing/schedule-price-changes-for-apps

**Source text (verbatim):**
> You may view or make changes to your upcoming price changes in App Store Connect at any time.
>
> - In Apps, select the app you want to view.
> - In the sidebar, under Monetization, click Pricing and Availability.
> - Under Price Schedule, view your upcoming changes and their start and end dates.
>
> The price schedule indicates whether Apple may make adjustments to pricing in certain countries or regions due to changes in taxes or foreign exchange rates. Countries or regions where pricing won’t be adjusted displays Manually Adjusted. When Apple automatically adjusts prices, you can locate the upcoming scheduled price details in the Price Schedule. Upcoming Apple reprices are marked Foreign Exchange or Tax Rate Adjustment.
>
> - You can delete scheduled price changes by hovering over the red delete button (-). In certain cases, such as upcoming tax or foreign exchange rate adjustments, or when a manually adjusted price is starting or reverting, you may not be able to remove an upcoming price change. Click the date of the price change for details.

**Applies to:** Apps with scheduled price changes

## BIZ.36 App pricing and availability

**Source page:** https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability/app-pricing-and-availability

**Source text (verbatim):**
> Pricing and availability properties determine where and when an app is available on the App Store and at what price. You can set these properties when you add an app to your account, or you can edit the app information later.
>
> | Property | Description |
> |---|---|
> | Price | Determines both the customer price and your proceeds. Your proceeds are the price minus Apple’s commission and applicable taxes. If you choose a price other than free, you must have a Paid Apps Agreement in place before you can sell the app. You can set a price or schedule price changes for apps. |
> | Start Date | The date when a new price will take effect on the App Store. |
> | End Date | The date that a price will no longer be in effect and will return to the previously set price. |
> | Make available for pre-order | Select this option to publish your app as a pre-order. The Pre-Orders section is only visible if your app has never been published on the App Store. |
> | Release Date | If you publish your app as a pre-order, this is the date when your app will end as a pre-order and become available for download on the App Store. This property is visible only when you select Make available for pre-order. |
> | Distribution for Education and Business | You may choose to distribute your app outside of the App Store to specific users as a custom app, or to business or educational institutions through Apple Business or Apple School Manager, where your app can be offered at a discount. |
> | Available at a reduced price for educational institutions | You can enable a 50% discount for educational institutions that purchase 20 or more copies of your iOS app or Mac app. Learn how to build apps for educations. |
> | Available for education and business without a reduced price | Your app will be available for Apple Business and Apple School Manager without a reduced price. For more information, visit Distributing Custom Apps for Business or Building Apps for Education. |
> | Available privately as a custom app (iOS only) | Select this option if you'd like to distribute your app as a custom app. This option is only available if your app hasn’t been approved yet. |
> | Availability | The storefronts where the app is available to purchase or download. |
> | Tax category | The category of the app for tax purposes. If you choose not to make any changes, your app and In-App Purchases will be assigned the App Store software category. |
> | Last Compatible Version Settings | The versions of an app that are available for existing customers to download from iCloud. You need to exclude app versions from iCloud if the version includes legal or usability issues. |

**Applies to:** All apps

- **[BIZ-55]** If an earlier app version includes legal or usability issues, has it been excluded from iCloud downloads for existing customers?
  - quote: "You need to exclude app versions from iCloud if the version includes legal or usability issues."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Pricing and Availability > Last Compatible Version Settings: versions available for download from iCloud.
  - fix: Exclude the affected app versions from iCloud in Last Compatible Version Settings.

## BIZ.37 Manage availability for your app on the App Store

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store

**Source text (verbatim):**
> Before submitting your app for review on the App Store, you must set its availability. You can release your app in any of the 175 countries or regions where the App Store is available, and you can offer your app for pre-order in regions where it hasn’t yet been published.
>
> A customer’s Apple Account country or region setting determines the App Store country or region where they can purchase apps. For example, if an account is set to Japan, purchases are limited to apps from the Japanese App Store.
>
> Your app may not be available for download or use in some countries or regions due to legal or regulatory requirements. View your app's App Store statuses to learn more.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** All apps distributed on the App Store

- **[BIZ-27]** Has the app’s availability been set before submitting it for review?
  - quote: "Before submitting your app for review on the App Store, you must set its availability."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Pricing and Availability > App Availability section: availability is configured (no Set Up Availability button remaining).
  - fix: Pricing and Availability > App Availability > Set Up Availability; choose All Countries or Regions, Specific Countries or Regions, or Publish as Pre-Order; confirm.

## BIZ.38 Set up availability for your app on the App Store

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability, then scroll to the App Availability section.
> - Click Set Up Availability.
> - Choose whether your app will be available for purchase or download on the App Store in All Countries or Regions, Specific Countries or Regions, or Publish as Pre-Order, then click Next.
>
> If you choose All Countries or Regions, click Confirm to make the app available in all 175 countries or regions of the App Store once it becomes Ready for Distribution. This will also ensure that your app is available in any new countries or regions added to the App Store in the future.
>
> If you choose Specific Countries or Regions, select the countries or regions where you want to make your app available on the App Store. To ensure availability in all countries and regions to the App Store in the future, select the box at the bottom of the list. Click Next, then click Confirm to make the app available in your selected countries or regions once it becomes Ready for Distribution.
>
> Note: Once your app becomes available for download or purchase on the App Store in a country or region, pre-orders are no longer possible in that same location.
>
> If you choose Publish as Pre-Order, make your app available for pre-order by selecting a release date and the countries or regions where you want to make your pre-order available. Your app will automatically become available in any new countries or regions added to the App Store in the future. Learn more about offering your app for pre-order.

**Applies to:** All apps distributed on the App Store

- **[BIZ-28]** Does the selected availability (All Countries or Regions, Specific Countries or Regions, or Publish as Pre-Order, plus the future-countries option) match the intended launch markets?
  - quote: "Choose whether your app will be available for purchase or download on the App Store in All Countries or Regions, Specific Countries or Regions, or Publish as Pre-Order"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > App Availability > Manage: review the list of countries or regions and the box for future countries or regions.
  - fix: manual — requires developer decision/legal/business action

## BIZ.39 View the status of your app's availability on the App Store in a specific country or region

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store

**Source text (verbatim):**
> Once you've set up your app's availability, you can take the following steps to monitor the availability status for your app in all 175 countries or regions on the App Store.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability, then scroll to the App Availability section.
> - Under App Availability, click Manage.
> - Under Availability, view the App Store status for each country or region. Learn more about App Store availability statuses.

**Applies to:** Apps with availability set up

## BIZ.40 Edit your app’s availability on the App Store

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store

**Source text (verbatim):**
> You can manage your app’s availability on the App Store at any time in App Store Connect.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability, then scroll to the App Availability section.
> - Under App Availability, click Manage.
> - Under Availability, click Manage Availability.
> - In the dialog that appears, select or deselect countries or regions to change your app's availability. You can also change whether your app will be made available in all future countries or regions added to the App Store by selecting or deselecting the box at the bottom of the list of countries or regions.
>
> Note:  When you deselect a country or region where your app was available, the app will be removed from the App Store in that country or region. Users who previously downloaded your app from the App Store in that country or region will continue to receive app updates. The app can be redownloaded from a customer's purchase history as long as the necessary contract remains active.
>
> - Click Next, then confirm.
>
> The changes take effect immediately but may require up to 24 hours to be visible to all users.

**Applies to:** Apps changing availability

## BIZ.41 Remove your app from the App Store in all countries or regions

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability.
> - Scroll to the bottom of the page, and click Remove App From Sale.
> - In the dialog that appears, Click Remove to confirm.
>
> Your app will be removed from the App Store in all countries or regions within 24 hours. Users who previously downloaded your app from the App Store in that country or region will continue to receive app updates. The app can be redownloaded from a customer's purchase history as long as the necessary contract remains active.

**Applies to:** Apps being removed from sale

## BIZ.42 App Store pricing and availability start times by country or region

**Source page:** https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability/app-store-pricing-and-availability-start-times-by-country-or-region

**Source text (verbatim):**
> When you modify information aspects of your app, the dates and times these changes take effect on the App Store vary by country or region. This includes changes such as setting the availability of apps, In-App Purchases, and pre-orders, scheduling introductory and win-back offers, or adjusting prices.
>
> - Times listed in the table below adjust automatically for US daylight saving time observance. During this period, Coordinated Universal Time (UTC) release times move one hour earlier and reflect accurately for your selected date.
> - If you schedule a price change in App Store Connect for a date and time that has already passed in some countries or regions, the change takes effect immediately but may require up to 24 hours to display for all users.
>
> View release times based on your scheduled date in App Store Connect. Times are shown for the time zone of your browser, as well as UTC.

**Applies to:** Apps scheduling availability, pre-orders, offers, or price changes

## BIZ.43 Set distribution methods

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/set-distribution-methods

**Source text (verbatim):**
> In App Store Connect, you can choose between two distribution options for your app:
>
> Public Distribution: Your app will be publicly available on the App Store in the selected countries or regions. It can also be available to anyone for volume purchase through Apple Business or Apple School Manager. You can request to change your publicly available app to an unlisted app to make your app discoverable on the App Store only with a direct link. Learn about unlisted app distribution.
>
> Private Distribution: Your app will be available only on Apple Business or Apple School Manager to specific businesses and organizations that you specify in App Store Connect.
>
> Note: Once your app is approved, the distribution method can't be changed. However, you can change a publicly available app to an unlisted app. To switch from private to public distribution—or vice versa—you must create a new app record and resubmit your binary.

**Applies to:** All apps

- **[BIZ-29]** Is the chosen distribution method (Public or Private) the intended one before the app is approved?
  - quote: "Once your app is approved, the distribution method can't be changed."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Pricing and Availability > App Distribution Methods: Public or Private selected as intended.
  - fix: Select the correct method before approval; after approval, switching between private and public requires a new app record and resubmitting the binary.

## BIZ.44 Make your app available publicly on the App Store and for volume purchase

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/set-distribution-methods

**Source text (verbatim):**
> Required role: Account Holder, Admin or App Manager. View role permissions.
>
> Apps on the App Store are automatically available for volume purchase for the same price in Apple Business and Apple School Manager, where businesses and educational institutions can download them for distribution in bulk.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability.
> - Under App Distribution Methods, select Public.
> - To offer educational institutions a discount, select the checkbox “Offer a reduced price on Apple School Manager for volume purchases.” Your app will be available at 50% of its listed price for purchases of 20 or more units by educational institutions.
> - On the top right, click Save.
>
> Once your app is approved, it’ll be available on the App Store in the  selected countries or regions, and in the Apps and Books section of Apple Business or Apple School Manager.

**Applies to:** Apps distributed publicly on the App Store

## BIZ.45 Make an app available only to specific businesses or organizations

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/set-distribution-methods

**Source text (verbatim):**
> Required role: Account Holder, Admin or App Manager. View role permissions.
>
> If you don’t want individual users to be able to download your app from the App Store, you can restrict the availability of your app to only specific businesses or organizations. This includes the ability to distribute proprietary apps for internal use within your organization.
>
> You can specify one or more organizations that can view and download the app in Apple Business or Apple School Manager. They can then distribute it through Mobile Device Management or redemption codes.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability.
> - Under App Distribution Methods, select Private.
> - Under Type, choose either Organization ID or Apple Account, and enter the required information. Enter the Organization ID to make the app visible in the organization's Apple Business or Apple School Manager account. For businesses still using the legacy Volume Purchase Program, you can assign an app to their volume purchasing account.
> - In the top right, click Save.

**Applies to:** Apps distributed privately through Apple Business or Apple School Manager

- **[BIZ-30]** For private distribution, has the Organization ID or Apple Account of each intended organization been entered?
  - quote: "Under Type, choose either Organization ID or Apple Account, and enter the required information."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > App Distribution Methods: Private selected and at least one organization listed with Organization ID or Apple Account.
  - fix: Under App Distribution Methods select Private, choose Type, enter the Organization ID or Apple Account, click Save.

## BIZ.46 Make your app available only through a direct link

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/set-distribution-methods

**Source text (verbatim):**
> Required role: Account Holder, Admin, or App Manager. View role permissions.
>
> Apps that aren’t suited for public distribution can be made discoverable as unlisted on the App Store with a direct link. Unlisted apps don’t show in any categories, recommendations, charts, search results, or other listings in the App Store. You can also use this direct link within Apple Business and Apple School Manager.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability.
> - Under App Distribution methods, make sure your app’s availability is set to Public. If your app has been approved for private download on Apple Business or Apple School Manager, you must create a new app record in App Store Connect, upload your binary, and set the distribution method to Public before proceeding to the next step.
> - Submit your app for review, if you haven’t already.
>
> Note: Once your app is approved, the distribution method can't be changed. The only exception to this is to change your publicly available app to an unlisted app. To switch from private to public, or vice versa, you’ll need to create a new app record and resubmit your binary.
>
> - To receive an unlisted link, submit a request. Upon approval, your app's distribution method will change to Unlisted in the Pricing and Availability section of the app information page. Future versions of your app will remain unlisted.

**Applies to:** Apps intended for unlisted distribution

- **[BIZ-31]** For an app intended to be unlisted, is the distribution method set to Public before the unlisted request?
  - quote: "make sure your app’s availability is set to Public"
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > App Distribution Methods shows Public (after approval of the request it shows Unlisted).
  - fix: Set the method to Public; if the app was approved for private distribution, create a new app record, upload the binary, and set the method to Public.

## BIZ.47 FAQs

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/set-distribution-methods

**Source text (verbatim):**
> I currently have an app that is available privately in Apple Business and I’d like to make it available publicly on the App Store, can I change my app’s distribution method?
>
> No. Changing your app's distribution method from public to private, or vice versa, requires submitting a new app for review.
>
> Where can users download my app in volume?
>
> Downloading apps in volume requires either an Apple School Manager or Apple Business account. Apple Business and Apple School Manager are available in many countries and regions.

**Applies to:** Apps distributed through Apple Business or Apple School Manager

## BIZ.48 Unlisted app distribution

**Source page:** https://developer.apple.com/support/unlisted-app-distribution/

**Source text (verbatim):**
> Release your apps that aren’t suited for public distribution as unlisted on the App Store, discoverable only with a direct link. Unlisted apps don’t appear in any App Store categories, recommendations, charts, search results, or other listings. In addition, they can be accessed through Apple Business and Apple School Manager. Apps for partner sales tools, employee resources, or research studies are examples of good candidates for unlisted distribution.
>
> Distribute your app to:
>
> - Limited audiences (such as part-time employees, franchisees, partners, business affiliates, higher-education students, or conference attendees) through a standard link that’s usable on the App Store and Apple School Manager or Apple Business.
> - Employee-owned devices that aren’t eligible to be managed through Apple School Manager or Apple Business.
> - Managed and unmanaged devices.
> - All regions that are supported by the App Store.

**Applies to:** Apps intended for unlisted distribution

## BIZ.49 Requesting an unlisted app link

**Source page:** https://developer.apple.com/support/unlisted-app-distribution/

**Source text (verbatim):**
> Before you request unlisted app distribution, your app must either already be on the App Store or be ready for final distribution and submitted to App Review. Add a note in the Review Notes section of your submission to indicate that your app is intended for unlisted distribution. Then, submit a request for unlisted app distribution.
>
> Requests will be declined for unlisted distribution if your app hasn’t been submitted to App Review, or if your app is in a beta or prerelease state.
>
> If your app is currently distributed privately to specific organizations through Apple Business or Apple School Manager, you’ll need to create a new app record in App Store Connect, upload your binary, and set the distribution method as publicly available on the App Store before submitting your request. Learn about setting distribution methods.

**Applies to:** Apps intended for unlisted distribution

- **[BIZ-32]** For an app intended to be unlisted, does the submission’s Review Notes state that the app is intended for unlisted distribution?
  - quote: "Add a note in the Review Notes section of your submission to indicate that your app is intended for unlisted distribution."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > platform version > App Review Information > Notes.
  - fix: Add a note in Review Notes saying the app is intended for unlisted distribution, then submit the unlisted app distribution request.
- **[BIZ-33]** Has the app been submitted to App Review and is it not in a beta or prerelease state when requesting unlisted distribution?
  - quote: "Requests will be declined for unlisted distribution if your app hasn’t been submitted to App Review, or if your app is in a beta or prerelease state."
  - surface: asc
  - verify: App Store Connect: app version status is Waiting for Review or later (or the app is already on the App Store); the build is a final release build, not beta/prerelease.
  - fix: Submit a final build to App Review before requesting the unlisted link.

## BIZ.50 Distributing your unlisted app

**Source page:** https://developer.apple.com/support/unlisted-app-distribution/

**Source text (verbatim):**
> If your request is approved, you can continue with the usual app release process. Your app’s distribution method will change to Unlisted App in the Pricing and Availability section of the app record, and will apply to any future versions of the app. A link will be generated to access your app on the App Store and on Apple Business or Apple School Manager. If your app is already available on the App Store, its current link will remain the same. If you decide to use a URL shortener, test the shortened link to ensure that it resolves correctly.
>
> Unlisted apps are available to anyone who has access to the link. Consider implementing a mechanism within your app to prevent unauthorized use.

**Applies to:** Apps approved for unlisted distribution

## BIZ.51 Publish for pre-order

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> Before releasing your app on the App Store in a new country or region, you can choose to make it available for pre-order. This allows customers to view your product page and order the app before it's released for download.

**Applies to:** Apps offered for pre-order

## BIZ.52 Eligibility

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> You can offer your app for pre-order in any country or region on the App Store where the app hasn't yet been released. Both free and paid apps across all Apple platforms are eligible for pre-orders. In-App Purchases aren’t eligible for pre-order, but you can set up your In-App Purchases, including promotional metadata, in App Store Connect before and during the pre-order period so that everything is ready once your app is released for download. Promoted In-App Purchases don’t display on your App Store product page until your app is released for download.
>
> App bundles aren’t eligible for pre-order. An app offered for pre-order must have at least one country or region where it’s already Ready for Sale to be included in a new app bundle.

**Applies to:** Apps offered for pre-order

- **[BIZ-34]** Is the pre-order configured only for countries or regions where the app hasn’t yet been released?
  - quote: "You can offer your app for pre-order in any country or region on the App Store where the app hasn't yet been released."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > App Availability > Manage: pre-order countries or regions do not include ones where the app is already available.
  - fix: Remove already-released countries or regions from the pre-order selection.
- **[BIZ-35]** If the app is offered for pre-order and is being included in a new app bundle, is it already Ready for Sale in at least one country or region?
  - quote: "An app offered for pre-order must have at least one country or region where it’s already Ready for Sale to be included in a new app bundle."
  - surface: asc
  - verify: App Store Connect > App Bundles: check whether a new bundle includes this pre-order app; check the app’s App Store status per country or region.
  - fix: Do not include the app in a new app bundle until it is Ready for Sale in at least one country or region.

## BIZ.53 Customer experience

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> Customers can start pre-orders on devices running iOS 11.2, iPadOS 13, macOS 10.13.2, tvOS 11.2, and watchOS 6, or later. Users with earlier operating systems can access product pages through direct links but will find the Buy button disabled, prompting them to update their OS to proceed with pre-orders.
>
> Customers can cancel their pre-orders in their App Store settings on iOS and macOS, and on a Windows PC. Learn more.
>
> If your pre-order’s release date is less than 180 days from the current date, the full release date appears on your app’s product page (for example, “Expected Jan 1, 2024”). For release dates more than 180 days away, only the month and year are displayed (for example, “Expected Jan 2024”).
>
> Customers who pre-order a paid app won't be charged until the app's official download release date. You may adjust the app's price during the pre-order phase; however, any price changes will result in customers being charged the lower amount—either the pre-order price they accepted or the price on the release date. Adjustments are subject to the original accepted terms.
>
> Once your app is released, customers receive a notification, and the app automatically downloads to the device used for pre-ordering. It’ll also download on their eligible devices if they turn on automatic downloads.
>
> Learn how to manage pre-orders using the App Store Connect API.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** Apps offered for pre-order

## BIZ.54 Publish your app for the first time as a pre-order

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> If this is your first time publishing an app in any country or region on the App Store, follow these steps to make your app available for pre-order.
>
> Note: Once your app is released for download or purchase on the App Store in a country or region, it can no longer be made available for pre-order in that same location.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability, then scroll to the App Availability section and click Set Up Availability.
> - Select Publish as Pre-Order, then click Next.
> - Choose a date to release your app for download, then click Next.
>
> Set your app's release date to fall between two and 180 days in the future. You may update the pre-order release date any time before the app is released on the App Store in your selected countries or regions.
>
> The date and time when your app is released on the App Store varies by country or region. Learn more about App Store pricing and availability start times by country or region.
>
> - Select the countries or regions where you want to make your pre-order available, then click Next.
> - Click Confirm. Your new pre-order will appear under the Pre-Orders section on the App Availability page. It won't appear on the App Store until you manually release an app version.
> - Click Pricing and Availability to return to the Pricing and Availability overview page, then click the platform version you want to submit for review.
> - Submit the app for review.
> - Once your app is approved and you're ready to make it available for pre-order, return to the platform version you want to release, then click Release This Version on the top right.
> - In the dialog that appears, click Confirm.
>
> Your pre-order publishes on the App Store immediately, but it may take up to 24 hours to appear to all users.
>
> If new countries or regions are added to the App Store in the future, your app will automatically be available for download or purchase there. You can manage this selection by editing your app's availability.

**Applies to:** Apps being published for the first time as a pre-order

- **[BIZ-36]** For a first-time pre-order, is the release date between two and 180 days in the future?
  - quote: "Set your app's release date to fall between two and 180 days in the future."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > App Availability > Pre-Orders: release date.
  - fix: Edit the pre-order release date to fall within the allowed window.
- **[BIZ-37]** For a first-time pre-order, is someone prepared to click Release This Version after approval so the pre-order appears on the App Store?
  - quote: "It won't appear on the App Store until you manually release an app version."
  - surface: asc
  - verify: App Store Connect > platform version: after approval, status Pending Developer Release; Release This Version button.
  - fix: After approval, open the platform version, click Release This Version, then Confirm.

## BIZ.55 Publish your app for pre-order in a new country or region

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> If you’ve already published your app to the App Store in a country or region, follow these steps to make your app available for pre-order in additional countries or regions.
>
> Note: Once your app is released for download or purchase on the App Store in a country or region, it can no longer be made available for pre-order in that same location.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability, then scroll to the App Availability section.
> - Under the App Availability section, click Manage.
> - Click Set Up Pre-Order. Or, if you already have an active pre-order for another country or region, click the add button (+) next to Pre-Orders.
> - Choose a date to release your app for download, then click Next.
>
> Set your app's release date to fall between two and 365 days in the future. You may update the pre-order release date any time before the app is released on the App Store in your selected countries or regions.
>
> The date and time when your app is released on the App Store varies by country or region. Learn more about App Store pricing and availability start times by country or region.
>
> - Select the countries or regions where you want to make your pre-order available, then click Next.
> - Click Confirm. Your new pre-order will appear under the Pre-Orders section on the Manage Availability page in App Store Connect.
>
> Pre-orders for your app will be published immediately on the App Store in the selected countries or regions. However, it may take up to 24 hours for the pre-order to appear for all users. The pre-order will be published using the version of the app that’s currently Ready for Distribution or Pre-Order Ready for Distribution.
>
> If new countries or regions are added to the App Store, your app will be made available for download or purchase there. You can manage this selection by editing your app's availability.

**Applies to:** Apps already published that add pre-orders in new countries or regions

- **[BIZ-38]** For a pre-order in a new country or region, is the release date between two and 365 days in the future?
  - quote: "Set your app's release date to fall between two and 365 days in the future."
  - surface: asc
  - verify: App Store Connect > Pricing and Availability > App Availability > Manage > Pre-Orders: release date.
  - fix: Edit the pre-order release date to fall within the allowed window.

## BIZ.56 Version updates during pre-order

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> You can update your app while it's available for pre-order by creating and submitting a new version in App Store Connect. Customers receive the latest app version that you've released for distribution. After submitting, you have the option to manually release the app version, set it for automatic release upon approval, or schedule it for release after a specific date. Learn more about an App Store version release options.
>
> If this is your first time releasing the app on the App Store or if you’ve chosen a manual release, you must follow these steps in App Store Connect once App Review approves the version:
>
> - In Apps, select the app you want to view.
> - In the sidebar, select the app version that has the status of Pending Developer Release.
> - On the top right, click Release This Version.
>
> Note: When you click Release This Version, the new app version will be released for download or purchase immediately in any country or region where the App Store status is Available or Available on App Release. If your app is available for pre-order, the new version will be published for pre-order in the specified countries or regions, but it won't go live until your pre-order release date.
>
> - In the dialog that appears, click Confirm.
>
> Your new version will be published on the App Store for pre-order immediately, but it may take up to 24 hours to appear to all users.

**Applies to:** Apps available for pre-order

## BIZ.57 Edit pre-order release date for your app

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> During the pre-order period, you can update the release date of your app. For first-time releases, the new publish date must be within 180 days of the pre-order's initial publication on the App Store in that specific country or region. If your app is already available for purchase or download in at least one country or region, the new pre-order release date must be within 365 days of the pre-order's first publication in that area.
>
> The release date and time of your app on the App Store may vary by region. Once the pre-order release date has passed in a particular country or region where your pre-order is published, you can’t alter the pre-order release date. Learn more about App Store pricing and availability start times by country or region.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability, then click Manage under the App Availability section.
> - Under the Countries or Regions column, click Edit next to the pre-order you want to edit.
> - When editing a pre-order for multiple countries or regions, you can choose which countries or regions will have their release date modified. If you wish to update the release date in all the countries or regions where your pre-order is set up, ensure all are selected.
> - Click Next, select “Edit your app’s release date,” then click Next again.
> - Select a new release date for your pre-order, then click Confirm.
>
> The updated release date will appear on the App Store within 24 hours.

**Applies to:** Apps available for pre-order

## BIZ.58 Release your app to customers immediately

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> During the pre-order period, you’re able to release your app to customers immediately, rather than waiting for the scheduled release date.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability, then under the App Availability section, click Manage.
> - Under the Countries or Regions column, click Edit next to the pre-order you want to edit.
> - When editing a pre-order for multiple countries or regions, you can choose which specific countries or regions you want the app to be released in immediately. To release the app in all countries or regions where you initially set up the pre-order, simply leave all checkboxes for countries or regions selected.
> - Click Next, select “Release your app to customers immediately," then click Next again.
> - Click Confirm.
>
> Your app will be released to the App Store immediately in the selected countries or regions but may take up to 24 hours to appear to all users. Customers who pre-ordered your app will be notified and your app will automatically download to their device. For paid apps, customers will be charged.

**Applies to:** Apps available for pre-order

## BIZ.59 Remove your pre-order offer from the App Store

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order

**Source text (verbatim):**
> Removing your pre-order offer from the App Store will result in customers not receiving the app, and they won’t be charged unless the app is made available for pre-order again before the release date. Furthermore, after the release date has passed, republishing your app as a pre-order won’t be possible.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability, then click Manage under the App Availability section.
> - Click Edit next to the pre-order you want to edit under the Countries or Regions column.
> - When editing a pre-order for multiple countries or regions, you can choose which specific countries or regions you want the app to be released in immediately. To release the app in all countries or regions where you initially set up the pre-order, simply leave all checkboxes for countries or regions selected.
> - Click Next, select “Remove your pre-order from the App Store," then click Next again.
> - Click Confirm.
>
> Your app will be removed from the App Store within 24 hours. Customers who pre-ordered your app won’t receive it, and paid customers won’t be charged unless you make your app available for pre-order again before the release date.

**Applies to:** Apps available for pre-order

## BIZ.60 Manage availability of iPhone and iPad apps on Macs with Apple silicon

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-macs-with-apple-silicon

**Source text (verbatim):**
> Users running macOS 11 or later on Macs with Apple silicon can access iPhone and iPad apps through the Mac App Store, provided no edits are made to the app availability. There's no porting process since these apps use the same frameworks, resources, and runtime environments as they do on iOS and iPadOS.
>
> When an app supports universal purchase and already has a presence on the Mac App Store through the macOS platform, you won’t have the option to offer the iOS app on the Mac App Store. Additionally, if your iOS app is available on the Mac App Store by using this option and you later add a macOS app by adding the macOS platform in App Store Connect, releasing it to the store will replace the iOS app on the Mac App Store. Existing users of the iOS app will be updated to the macOS app.
>
> You can choose to make your iPhone and iPad apps available, or not, on the Mac App Store for users running macOS 11 or later on Macs with Apple silicon. This is set at the app level and will apply to all versions of your app.
>
> Apple automatically calculates the minimum macOS version using the LSMinimumSystemVersion from your build (if applicable) and the macOS version corresponding to your build's MinimumOSVersion. If you’ve selected a minimum macOS version in Pricing and Availability that's higher than either the LSMinimumSystemVersion or the macOS version corresponding to the MinimumOSVersion, the version you selected will be displayed instead.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** iPhone and iPad apps

- **[BIZ-39]** Has a deliberate choice been made whether the iPhone/iPad app is available on the Mac App Store for Macs with Apple silicon (it is available unless edited)?
  - quote: "You can choose to make your iPhone and iPad apps available, or not, on the Mac App Store for users running macOS 11 or later on Macs with Apple silicon."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Pricing and Availability > iPhone and iPad Apps on Apple Silicon Mac > Apple Silicon Mac Availability: “Make this app available” checkbox state. If available, confirm the app functions as intended on a Mac with Apple silicon.
  - fix: manual — requires developer decision/legal/business action

## BIZ.61 Edit availability on an individual app basis

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-macs-with-apple-silicon

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability and scroll down to the iPhone and iPad Apps on Apple Silicon Mac section.
> - Under Apple Silicon Mac Availability, deselect “Make this app available” to opt out of offering your app on the Mac App Store. Select the checkbox if you want the app to be available on the Mac App Store.
>
> You can change the minimum macOS version required for compatibility in the menu. This selection also applies to tester groups enabled for testing iPhone and iPad apps on Macs with Apple silicon with TestFlight.
>
> - On the top right, click Save.

**Applies to:** iPhone and iPad apps

## BIZ.62 Edit availability for multiple apps at a time

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-macs-with-apple-silicon

**Source text (verbatim):**
> - In Apps, select iOS Apps on Mac Availability from the ellipsis menu (...) in the top left.
> - In the dialog that appears, deselect the iPhone and iPad apps you don’t want to make available on the Mac App Store.
> - Click Done.
>
> To opt out of offering any of your iPhone and iPad apps on the Mac App Store for users running macOS 11 or later on Macs with Apple silicon, click Don’t Make Available.

**Applies to:** iPhone and iPad apps

## BIZ.63 Verify your app’s compatibility with Macs with Apple silicon

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-macs-with-apple-silicon

**Source text (verbatim):**
> If your iPhone and iPad apps are compatible with Macs with Apple silicon and function as intended, verify them in App Store Connect to let users know they’ll receive a great experience on macOS. Once verified, this option will no longer be available in App Store Connect.
>
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability and scroll down to the iPhone and iPad Apps on Apple Silicon Mac section.
> - Under Compatibility with Apple Silicon Macs, click Verify Compatibility.
>
> Note: Compatibility with Apple Silicon Macs isn’t available if a build has never been uploaded for the platform.
>
> - In the dialog that appears, click Verify.
>
> Note: The Compatibility with Apple Silicon Macs section specifies whether your current and future app versions are compatible with Apple silicon Macs.

**Applies to:** iPhone and iPad apps compatible with Macs with Apple silicon

## BIZ.64 Manage availability of iPhone and iPad apps on Apple Vision Pro

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-apple-vision-pro

**Source text (verbatim):**
> Your iPhone and iPad apps will be available to users on Apple Vision Pro unless you edit their availability in App Store Connect. These apps will run natively, using the same frameworks, resources, and runtime environment as they do on iOS and iPadOS.
>
> If your iOS app offers universal purchase and also supports visionOS, the option to offer the iOS app on the App Store on Apple Vision Pro won’t be available. Additionally, if your iOS app is available on Apple Vision Pro through universal purchase and you add the visionOS platform in App Store Connect, publishing the visionOS version will replace the iOS version on Apple Vision Pro. Current users of the iOS app will automatically receive the visionOS update on Apple Vision Pro.
>
> You can choose to make your iPhone and iPad apps available or not available on the App Store for Apple Vision Pro. This is set at the app level and applies to all versions of your app.
>
> Note: Apps that have been in the Kids category can’t be made available on visionOS.
>
> Required role: Account Holder, Admin, or App Manager. View role permissions.

**Applies to:** iPhone and iPad apps

- **[BIZ-40]** Has a deliberate choice been made whether the iPhone/iPad app is available on the App Store for Apple Vision Pro (it is available unless edited)?
  - quote: "You can choose to make your iPhone and iPad apps available or not available on the App Store for Apple Vision Pro."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > Pricing and Availability > iPhone and iPad Apps on Apple Vision Pro > Apple Vision Pro Availability: “Make this app available on Apple Vision Pro” checkbox state.
  - fix: manual — requires developer decision/legal/business action
- **[BIZ-56]** If the app has been in the Kids category, is it understood that it can’t be made available on visionOS?
  - quote: "Apps that have been in the Kids category can’t be made available on visionOS."
  - surface: asc
  - verify: App Store Connect > Apps > [app] > App Information > Category (current and past); Pricing and Availability > iPhone and iPad Apps on Apple Vision Pro.
  - fix: manual — requires developer decision/legal/business action

## BIZ.65 Edit availability on an individual app basis

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-apple-vision-pro

**Source text (verbatim):**
> - In Apps, select the app you want to view.
> - In the sidebar, click Pricing and Availability.
> - On the right, the iPhone and iPad Apps on Apple Vision Pro section appears.
> - Under Apple Vision Pro Availability, deselect “Make this app available on Apple Vision Pro” to opt out of offering your app on the App Store on Apple Vision Pro. Select the checkbox to make your app available on the App Store on Apple Vision Pro.
> - On the top right, click Save.

**Applies to:** iPhone and iPad apps

## BIZ.66 Edit availability for multiple apps at a time

**Source page:** https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-apple-vision-pro

**Source text (verbatim):**
> - In Apps, select iOS Apps on Apple Vision Pro Availability from the ellipsis menu (…) in the top left.
> - In the dialog that appears, deselect the iOS apps you do not want to make available on the App Store on Apple Vision Pro.
> - Click Save.
>
> To opt out of offering any of your iPhone and iPad apps on the App Store on Apple Vision Pro, click None.

**Applies to:** iPhone and iPad apps

## BIZ.67 Set your developer name

**Source page:** https://developer.apple.com/help/app-store-connect/create-an-app-record/set-your-developer-name

**Source text (verbatim):**
> By default, your legal name is used as your developer name. If you enrolled in the Apple Developer Program as an organization, you can set a different developer name if it's a registered trade name, DBA, or fictitious business name. For example, if your legal name is “Apps Company LLC”, your trade name can simply be “Apps Company”, which is used for distribution.
>
> If you’re enrolled as an individual, this option isn’t available to you and the developer name is the same as your legal name.
>
> You can set your developer name only when adding an app to your account for the first time. You can't edit or update this name later, so it's important to enter it correctly.
>
> - In Apps, click the Add button (+).
>
> The Apps page is blank until you create your first app.
>
> - In the pop-up window, enter your developer name into the Company Name field.
> - Fill in the other required details, then click Create.
>
> Once your app is approved, your developer name appears under your app name on App Store product pages and displays when users install your app.

**Applies to:** Developers adding an app to their account for the first time

- **[BIZ-41]** Is the developer name (Company Name field) correct before the first app record is created?
  - quote: "You can't edit or update this name later, so it's important to enter it correctly."
  - surface: asc
  - verify: App Store Connect > Apps > Add (+) > New App dialog > Company Name field (shown only when creating the first app).
  - fix: manual — requires developer decision/legal/business action
- **[BIZ-42]** If an organization uses a developer name different from its legal name, is it a registered trade name, DBA, or fictitious business name?
  - quote: "you can set a different developer name if it's a registered trade name, DBA, or fictitious business name"
  - surface: manual
  - verify: Compare the intended developer name with the organization’s registration documents.
  - fix: manual — requires developer decision/legal/business action

## BIZ.68 Role permissions

**Source page:** https://developer.apple.com/help/app-store-connect/reference/account-management/role-permissions

**Source text (verbatim):**
> The tasks you're able to perform depends on your user role. The Account Holder can access all aspects of App Store Connect and the Apple Developer website, and is the only user that can sign legal agreements, renew membership, request access to the App Store Connect API, remove auto-renewable subscriptions from sale, submit Safari Extensions, or create developer ID certificates.
>
> Members of an organization’s team in the Apple Developer Program also have access to membership resources on the Apple Developer website and other membership benefits. Users who have been given access to App Store Connect by an individual enrolled in the Apple Developer Program only have access to App Store Connect.
>
> | Role | Description |
> |---|---|
> | Account Holder | The person who completes program enrollment is assigned the Account Holder role. This user is responsible for entering into legal agreements with Apple. |
> | Admin | Serves as a secondary contact for teams and has many of the same responsibilities as the Account Holder. Admins have access to all apps. If the Admin is part of an organization team, they have Certificates, Identifiers & Profiles by default. |
> | Finance | Manages financial information, including downloading reports and uploading tax forms. They can view all apps in Payments and Financial Reports, Sales and Trends, and App Analytics. |
> | App Manager | Manages all aspects of an app, such as pricing, App Store information, and app development and delivery. |
> | Developer | Manages development and delivery of an app. |
> | Marketing | Manages marketing materials and promotional artwork. They’ll be contacted by Apple if your app is considered for featuring on the App Store. |
> | Sales | Analyzes sales, downloads, and other analytics for an app. |
> | Customer Support | Analyzes and responds to customer reviews on the App Store. |
>
> Learn which roles have access to specific functionality within App Store Connect.

**Applies to:** All teams

- **[BIZ-43]** Is the Account Holder available to sign the legal agreements (such as the Paid Apps Agreement) needed before submission?
  - quote: "is the only user that can sign legal agreements"
  - surface: manual
  - verify: App Store Connect > Users and Access: identify the user with the Account Holder role and confirm they can sign in and act.
  - fix: Have the Account Holder sign the pending agreements in Business > Agreements.

## BIZ.69 Account Holder

**Source page:** https://developer.apple.com/help/account/access/roles/

**Source text (verbatim):**
> If you’re enrolled in a developer program as an organization, the Account Holder for your team manages the account and is the person who needs to renew your annual program membership, accept legal agreements on behalf of your organization, initially add Admins to the team, and approve banking changes in your account.
>
> Membership renewal. If the Account Holder enrolled through the Apple Developer app, your membership will renew on its own as an auto-renewable subscription. If the Account Holder enrolled through the Apple Developer website, they can opt in to automatically renew through the Apple Developer app or website*, or manually renew on the website.
>
> Updated agreements. From time to time, Apple may update the Apple Developer Program License Agreement, or an addendum to it, to support new features or policies. When an agreement is updated, your Account Holder will be notified and must accept the agreement on behalf of your organization. To maintain full access to membership resources, such as Certificates, Identifiers & Profiles, App Store Connect, and the App Store Connect API, your Account Holder will need to agree to the updated terms by the date noted on your developer account landing page.
>
> Additional agreements. In cases where enabling a capability or service requires additional terms, your Account Holder must agree to them on behalf of your organization. For example, to sell paid apps or offer In-App Purchases on the App Store, your Account Holder will need to sign the Paid Applications Agreement.

**Applies to:** Apple Developer Program teams

- **[BIZ-44]** Has the Account Holder agreed to any updated Apple Developer Program License Agreement terms by the date noted on the developer account?
  - quote: "your Account Holder will need to agree to the updated terms by the date noted on your developer account landing page."
  - surface: asc
  - verify: Apple Developer account landing page and App Store Connect: look for an updated-agreement notice.
  - fix: Account Holder reviews and accepts the updated agreement in the developer account.

## BIZ.70 Business

**Source page:** https://developer.apple.com/help/account/access/roles/

**Source text (verbatim):**
> |  | Account Holder | Admin | App Manager | Developer | Finance | Marketing | Sales | Customer Support |
> |---|---|---|---|---|---|---|---|---|
> | Manage Business | Full access. | Full access. |  |  | Full access. |  |  |  |
> | Sign agreements | Full access. |  |  |  |  |  |  |  |

**Applies to:** Apple Developer Program teams

## BIZ.71 Apps

**Source page:** https://developer.apple.com/help/account/access/roles/

**Source text (verbatim):**
> |  | Account Holder | Admin | App Manager | Developer | Finance | Marketing | Sales | Customer Support |
> |---|---|---|---|---|---|---|---|---|
> | Create app records | Full access. | Full access. | Full access. | Requires access to create app records, granted in Users and Access |  | Requires access to create app records, granted in Users and Access. |  |  |
> | Upload builds | Full access. | Full access. | Requires access to Certificates, Identifiers & Profiles, granted in Users and Access. Includes access to CloudKit Console. | Requires access to Certificates, Identifiers & Profiles, granted in Users and Access. Includes access to CloudKit Console. |  |  |  |  |
> | Upload Apple-hosted asset packs | Full access. | Full access. | Full access. | Full access. |  |  |  |  |
> | Create app versions | Full access. | Full access. | Full access. |  |  | Full access. |  |  |
> | Submit apps | Full access. | Full access. | Full access. |  |  |  |  |  |
> | Edit App Store details* | Full access. | Full access. | Full access. |  |  | Full access. |  | Full access. |
> | Edit App Clip details | Full access. | Full access. | Full access. |  |  | Full access. |  |  |
> | Edit app pricing and availability | Full access. | Full access. | Full access. |  |  | Read-only access. |  |  |
> | Respond to app privacy questions | Full access. | Full access. | Full access. |  |  |  |  |  |
> | View app accessibility support | Full access. | Full access. | Full access. | Full access. |  | Full access. |  |  |
> | Manage app accessibility support | Full access. | Full access. | Full access. |  |  | Full access. |  |  |
> | Transfer apps | Full access. |  |  |  |  |  |  |  |
> | Remove and restore apps | Full access. | Full access. |  |  |  |  |  |  |
> | Reset summary rating | Full access. | Full access. | Full access. |  |  |  |  |  |
> | Create in‑app purchases | Full access. | Full access. | Full access. | Full access. |  | Full access. |  |  |
> | Submit in‑app purchases | Full access. | Full access. | Full access. |  |  |  |  |  |
> | Edit in‑app purchases | Full access. | Full access. | Full access. | Read-only access. |  |  |  |  |
> | Create in‑app events | Full access. | Full access. | Full access. |  |  | Full access. |  |  |
> | Submit in‑app events | Full access. | Full access. | Full access. |  |  | Can submit if there’s no app binary in the submission. |  |  |
> | Manage Game Center | Full access. | Full access. | Full access. | Full access. |  | Full access. |  |  |
> | Manage leaderboard scores | Full access. | Full access. | Full access. |  |  |  |  |  |
> | Manage promo codes and promo art | Full access. | Full access. | Full access. |  |  | Full access. |  |  |
> | Set or change pricing and availability for auto-renewable subscriptions | Full access. | Full access. | Full access. |  |  |  |  |  |
> | Generate receipt validation codes for auto-renewable subscriptions | Full access. | Full access. |  |  |  |  |  |  |
> | Enable server notifications for auto-renewable subscriptions | Full access. | Full access. | Full access. |  |  | Full access. |  |  |
> | Remove auto-renewable subscriptions from sale | Full access. |  |  |  |  |  |  |  |
> | Edit Purchase Options - Update market settings (Apple Business, Apple School Manager) | Full access. | Full access. | Full access. |  |  |  |  |  |
> | Remove Apple Business Manager and/or Apple School Manager from Purchase Options | Full access. |  |  |  |  |  |  |  |
> | Edit Purchase Options - Multiseat subscriptions | Full access. | Full access. | Full access. |  |  |  |  |  |
> | Enable and disable billing grace period for your app | Full access. | Full access. | Full access. |  |  |  |  |  |
> | Manage TestFlight builds | Full access. | Full access. | Full access. | Read-only access. |  | Read-only access. |  |  |
> | Manage external TestFlight groups and add builds | Full access. | Full access. | Full access. | Read-only access. |  | Read-only access. |  |  |
> | Manage internal TestFlight groups and add builds | Full access. | Full access. | Full access. | Full access. |  | Full access. |  |  |
> | Manage TestFlight App Clip experiences | Full access. | Full access. | Full access. | Read-only access. |  | Read-only access. |  |  |
> | Create, edit, and submit Nominations | Full access. | Full access. | Full access. |  |  | Full access. |  |  |
> | View ratings and reviews | Full access. | Full access. | Full access. | Full access. |  | Full access. |  | Full access. |
> | Respond to customer reviews | Full access. | Full access. |  |  |  |  |  | Full access. |
> | Report a Concern | Full access. | Full access. | Full access. |  |  |  |  | Full access. |
> | Respond to App Review | Full access. | Full access. | Full access. | Read-only access. |  | Read-only access. |  |  |
>
> *App Store details include metadata on the App Information page, the platform Version Information page, and the privacy policy URLs.

**Applies to:** Apple Developer Program teams

- **[BIZ-45]** Does the person submitting the app hold a role with Submit apps access (Account Holder, Admin, or App Manager)?
  - quote: "Submit apps"
  - surface: asc
  - verify: App Store Connect > Users and Access: role of the submitting user (and app access, if limited to certain apps).
  - fix: Account Holder or Admin assigns the Admin or App Manager role, or a user with such a role performs the submission.
- **[BIZ-46]** Does the person uploading builds hold Account Holder or Admin, or App Manager/Developer with access to Certificates, Identifiers & Profiles granted in Users and Access?
  - quote: "Upload builds"
  - surface: asc
  - verify: App Store Connect > Users and Access > [user]: role and the Certificates, Identifiers & Profiles access setting.
  - fix: Grant access to Certificates, Identifiers & Profiles to the App Manager or Developer user in Users and Access, or upload as Account Holder/Admin.

## BIZ.72 View China mainland compliance information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-compliance-information/view-china-mainland-compliance-information

**Source text (verbatim):**
> If you're an organization based in China mainland, the Anti Telecom Fraud Law and Cybersecurity Law require Apple to collect and verify identification information for the purpose of displaying on your apps’ product pages. Apple will automatically display the following additional information on product pages on the App Store in China mainland:
>
> Organizations
>
> - Company name in Chinese. The name associated with your Dun & Bradstreet (D-U-N-S) profile is automatically displayed.
> - China Unified Social Credit Identifier (USCI). The USCI associated with your D-U-N-S Number will automatically display. If you need to update the USCI associated with your D-U-N-S Number, or if you don't have a D-U-N-S number associated with your developer account but wish to display your USCI, contact D&B to update or create your D-U-N-S account information. (If you have a D-U-N-S number with the correct USCI, and don’t see the USCI reflected on your apps product page, contact us.)
>
> Learn more about the Anti Telecom Fraud Law and Cybersecurity Law.

**Applies to:** Organizations based in China mainland

- **[BIZ-47]** For an organization based in China mainland, are the Chinese company name and USCI associated with the D-U-N-S profile correct?
  - quote: "The USCI associated with your D-U-N-S Number will automatically display."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab > Compliance section > China Mainland: review the company name in Chinese and USCI.
  - fix: Contact D&B to update or create the D-U-N-S account information; if the D-U-N-S number has the correct USCI but it is not shown, contact Apple.

## BIZ.73 View Anti Telecom Fraud Law compliance information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-compliance-information/view-china-mainland-compliance-information

**Source text (verbatim):**
> Required role: Account Holder or Admin. View role permissions.
>
> - Select Business at the top of the page.
> - On the Agreements tab, scroll down to the Compliance section.
> - Click on China Mainland.
> - Confirm your information, and click Done.

**Applies to:** Organizations based in China mainland

- **[BIZ-48]** Has the Account Holder or Admin confirmed the China Mainland compliance information?
  - quote: "Confirm your information, and click Done."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab > Compliance section > China Mainland.
  - fix: Open China Mainland in the Compliance section, confirm the information, click Done.

## BIZ.74 Manage Korea compliance information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-korea-compliance-information

**Source text (verbatim):**
> If you're an individual or organization based in South Korea, the Act on Consumer Protection in Electronic Commerce requires Apple to collect and verify identification information for the purpose of displaying on your apps’ product pages. The information you need to provide depends on whether you’re enrolled in the Apple Developer Program as an individual or organization.
>
> Organizations
>
> You’ll need to enter the following for display on your App Store product pages:
>
> - Company name
> - Email address
> - Phone number
> - Business registration number (BRN). If you’ve signed the Paid Applications Agreement, the BRN you entered in the Korean Tax Forms section of Business will automatically display. If you don’t currently offer paid content on the App Store and haven’t signed the Paid Applications Agreement but would like to display a BRN number, you can provide your BRN using the steps below.
>
> Individuals
>
> You’ll need to enter the following for display on your App Store product pages:
>
> - Email address
> - Business registration number (BRN). If you've signed the Paid Applications Agreement, the BRN you entered in the Korean Tax Forms section of Business will automatically display. If you don’t currently offer paid content on the App Store and haven’t signed the Paid Applications Agreement but would like to display a BRN number, you can provide your BRN using the steps below.

**Applies to:** Individuals or organizations based in South Korea

- **[BIZ-49]** For a developer based in South Korea, has the identification information required for display on product pages been entered (organizations: company name, email, phone, BRN; individuals: email, BRN)?
  - quote: "the Act on Consumer Protection in Electronic Commerce requires Apple to collect and verify identification information for the purpose of displaying on your apps’ product pages"
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab > Compliance section > Korean Law.
  - fix: Account Holder or Admin: Compliance > Korean Law; verify and validate phone number and email, provide BRN if needed, click Confirm.

## BIZ.75 Enter or edit your identification information

**Source page:** https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-korea-compliance-information

**Source text (verbatim):**
> Required role: Account Holder or Admin. View role permissions.
>
> - Select Business at the top of the page.
> - On the Agreements tab, scroll down to the Compliance section.
> - Click Korean Law.
> - Verify your phone number and email address and make any required changes.
>
> If needed, check the box to provide your Business registration number, then click Next. You’ll be able to enter your BRN in the next step.
>
> - Validate the phone number you provided on the previous screen. If your phone number cannot receive authentication codes, you can request manual verification. Once you’re done, you’ll automatically be directed to the next step.
> - Validate the email address you provided. Once you’re done, you’ll automatically be directed to the next step.
> - Confirm your contact information for Korea, and click Confirm.
>
> Note: Organizations have the option to upload a copy of a business or court document that validates an email and phone number. You may also choose to provide this information in a letter on official letterhead. Ensure that the letter:
>
> - States that you have the legal authority to bind your organization to all legal agreements.
> - States that your organization has the intent to distribute apps to customers in Korea.
> - Provides your printed name, title, signature, and your organization’s contact phone number, and email address.

**Applies to:** Individuals or organizations based in South Korea

## BIZ.76 Compliance review

**Source page:** https://developer.apple.com/help/app-store-connect/reference/account-management/compliance-review

**Source text (verbatim):**
> When you join the Apple Developer Program, Apple is obligated to verify the information you provide to ensure that neither you nor your organization are doing business in any embargoed countries, or listed on any restricted party lists published by governments.
>
> There are different types of compliance reviews:
>
> - Individual or user review: Provide a valid government issued ID for the individual or user. You won't have access to any module in App Store Connect until the review is complete.
>
> Note: Please ensure that the name on your Apple Account matches the name on the ID provided.
>
> - Legal entity review: Provide business registration or a certificate of incorporation document. You may not be able to sign pending agreements or submit new apps or app updates until review is complete.
> - Bank account review: Provide a valid government issued ID for the Account Holder that matches the name on the bank account for individual accounts or a business registration or a certificate of incorporation document for company accounts. You may not be able to update your banking information or receive payments until review is complete.
>
> The Account Holder is responsible for submitting documentation for compliance reviews. Compliance reviews are standard for all Developer Program members and we aim to make these quick and efficient. To help streamline the review process, please ensure you're responding promptly to requests, using English (if available) for documents, and double-checking submissions. Please note that Apple periodically re-performs compliance reviews, including when you make changes to information related to your Developer Account.
>
> You can track your compliance status in the Business module of App Store Connect. If your case is still pending after 14 business days, please contact us.

**Applies to:** All Apple Developer Program members

- **[BIZ-50]** Is there no pending legal entity compliance review that could prevent signing pending agreements or submitting the app or update?
  - quote: "You may not be able to sign pending agreements or submit new apps or app updates until review is complete."
  - surface: asc
  - verify: App Store Connect > Business module: compliance status.
  - fix: Account Holder submits the requested business registration or certificate of incorporation document; contact Apple if still pending after 14 business days.
- **[BIZ-51]** Is there no pending individual or user compliance review blocking access to App Store Connect modules?
  - quote: "You won't have access to any module in App Store Connect until the review is complete."
  - surface: asc
  - verify: App Store Connect > Business module: compliance status.
  - fix: Provide a valid government-issued ID whose name matches the Apple Account name.
- **[BIZ-52]** If the app earns money, is there no pending bank account compliance review blocking banking updates or payments?
  - quote: "You may not be able to update your banking information or receive payments until review is complete."
  - surface: asc
  - verify: App Store Connect > Business module: compliance status.
  - fix: Account Holder provides the requested ID or business registration document.

## BIZ.77 Manage information for State Council Decree No. 810

**Source page:** https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-information-for-state-council-decree-no-810

**Source text (verbatim):**
> As required by the Provisions on the Reporting of Tax-related Information by Internet Platform Enterprises (State Council Decree No. 810), Apple collects specific information from Chinese content providers who distribute apps through App Store and submit this information to the State Taxation Administration (STA).
>
> Apple is required to report Chinese developers who distribute apps through the App Store from July 2025 onwards.
>
> Required role: Account Holder or Admin. View role permissions.
>
> - Select Business at the top of the page.
> - On the Agreements tab, scroll down to the Compliance section.
> - Next to State Council Decree No. 810 click Add Info.
> - Enter your Resident ID Card Number and Name on Resident ID Card (if prompted). Then click Done.
>
> It's your responsibility to keep your account information available to Apple up to date.
>
> You’ll need to ensure you have provided a DUNS number and Unified Social Credit Identifier (USCI) for State Council Decree No. 810. If you’re missing either of these, there will be a banner displayed in the Business section of App Store Connect. To provide your DUNS number, you’ll be directed to enter it on the company information page. If you have entered a DUNS number, but need to provider your USCI, then you’ll need to go to the Dun & Bradstreet support page.

**Applies to:** Chinese developers who distribute apps through the App Store

- **[BIZ-57]** For a Chinese individual developer, has the Resident ID Card Number (and Name on Resident ID Card, if prompted) been entered for State Council Decree No. 810?
  - quote: "Enter your Resident ID Card Number and Name on Resident ID Card (if prompted). Then click Done."
  - surface: asc
  - verify: App Store Connect > Business > Agreements tab > Compliance section > State Council Decree No. 810: information entered (no Add Info button pending).
  - fix: Account Holder or Admin: Compliance > State Council Decree No. 810 > Add Info; enter the Resident ID details, click Done.
- **[BIZ-58]** For a Chinese company, have a DUNS number and USCI been provided for State Council Decree No. 810 (no missing-information banner in Business)?
  - quote: "You’ll need to ensure you have provided a DUNS number and Unified Social Credit Identifier (USCI) for State Council Decree No. 810."
  - surface: asc
  - verify: App Store Connect > Business: no banner about a missing DUNS number or USCI.
  - fix: Enter the DUNS number on the company information page; to provide the USCI, go to the Dun & Bradstreet support page.

## Sources

- https://developer.apple.com/help/app-store-connect/
- https://developer.apple.com/help/app-store-connect/manage-agreements/sign-and-update-agreements
- https://developer.apple.com/help/app-store-connect/manage-agreements/view-agreements-status
- https://developer.apple.com/help/app-store-connect/manage-banking-information/enter-banking-information
- https://developer.apple.com/help/app-store-connect/manage-tax-information/provide-tax-information
- https://developer.apple.com/help/app-store-connect/manage-app-information/set-a-tax-category
- https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price
- https://developer.apple.com/help/app-store-connect/manage-app-pricing/schedule-price-changes-for-apps
- https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability/app-pricing-and-availability
- https://developer.apple.com/help/app-store-connect/reference/pricing-and-availability/app-store-pricing-and-availability-start-times-by-country-or-region
- https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-for-your-app-on-the-app-store
- https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/set-distribution-methods
- https://developer.apple.com/support/unlisted-app-distribution/
- https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/publish-for-pre-order
- https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-macs-with-apple-silicon
- https://developer.apple.com/help/app-store-connect/manage-your-apps-availability/manage-availability-of-iphone-and-ipad-apps-on-apple-vision-pro
- https://developer.apple.com/help/app-store-connect/create-an-app-record/set-your-developer-name
- https://developer.apple.com/help/app-store-connect/reference/account-management/role-permissions
- https://developer.apple.com/support/roles/
- https://developer.apple.com/help/account/access/roles/
- https://developer.apple.com/help/app-store-connect/manage-compliance-information/view-china-mainland-compliance-information
- https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-korea-compliance-information
- https://developer.apple.com/help/app-store-connect/reference/account-management/compliance-review
- https://developer.apple.com/help/app-store-connect/manage-compliance-information/manage-information-for-state-council-decree-no-810
