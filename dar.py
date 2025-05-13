import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Définir les paires de dialogues
pairs = [
    ["Quel est le plat du jour ?", ["🍽️ Le plat du jour est le couscous, un délicieux plat du chef. 😋"]],
    ["Quels sont vos horaires d'ouverture ?", ["⏰ Nous sommes ouverts :\n- Lundi à Vendredi : 08h30 - 22h00\n- Samedi : 10h00 - 23h00\n- Dimanche : 09h00 - 21h00."]],
    ["Avez-vous des options végétariennes ou véganes ?", ["🥗 Oui, nous avons plusieurs options végétariennes et véganes disponibles. 🌱 Vous pouvez les consulter sur notre menu."]],
    ["Puis-je réserver une table pour ce soir ?", ["📞 Bien sûr ! Vous pouvez réserver une table en ligne ou nous appeler directement pour confirmer votre réservation. 📅"]],
    ["Quel est le prix moyen d'un repas dans votre restaurant ?", ["💵 Le prix moyen d'un repas chez nous est d'environ 40DH."]],
    ["Est-ce que vous proposez des plats sans gluten ?", ["🌾🚫 Oui, nous proposons plusieurs plats sans gluten. N'hésitez pas à demander à notre serveur pour plus de détails."]],
    ["Faites-vous des livraisons ou des commandes à emporter ?", ["🚗💨 Oui, nous offrons des services de livraison et de commande à emporter. Vous pouvez passer votre commande en ligne ou par téléphone. 📱"]],
    ["Puis-je voir votre menu en ligne ?", ["📄 Oui, vous pouvez consulter notre menu directement sur notre site web. 🌐"]],
    ["Quels desserts proposez-vous ?", ["🍰 Nous proposons une sélection de desserts maison, comme Jawhara, Chebbakia, Mhalabia et bien d'autres. 🍯"]],
    ["Acceptez-vous les paiements par carte bancaire ?", ["💳 Oui, nous acceptons les paiements par carte bancaire, y compris les cartes de crédit et de débit."]],
    ["Y a-t-il des promotions spéciales cette semaine ?", ["🎉 Oui, nous avons une promotion spéciale cette semaine : -20% sur chaque plat à l'occasion du nouvel an. 🥂"]],
    ["Est-ce que vous avez un menu enfant ?", ["👶 Oui, nous avons un menu enfant adapté, avec des plats simples et savoureux. 🍟"]],
    ["Avez-vous des options pour les allergies alimentaires ?", ["⚠️ Nous prenons en compte les allergies alimentaires. Merci de nous informer de vos allergies, et nous vous proposerons des options adaptées. 🩺"]],
    ["Puis-je modifier ma commande après l'avoir passée ?", ["✏️ Cela dépend de l'état de votre commande. Si elle n'a pas encore été préparée, nous serons heureux de la modifier. 😊"]],
    ["Quels sont les plats les plus populaires chez vous ?", ["🔥 Nos plats les plus populaires sont les tajines, ils sont toujours très appréciés par nos clients. 🍲"]],
]

# Initialiser le chatbot
chat = Chat(pairs, reflections)

st.set_page_config(
    page_title="Votre Tajinebot",
    page_icon="🤖🍲",  # Exemple d'icône emoji
    layout="centered"
)
# Titre de l'application
st.title("Bienvenue chez Dar Tajine 🍲")

# Image de bannière
st.image("logo-removebg-preview.png",use_container_width=True)

# Configurer l'interface Streamlit
st.write("Posez une question à notre Tajinebot et il vous répondra.")

# Entrée utilisateur
user_input = st.text_input("Vous :")

# Réponse du chatbot
if user_input:
    response = chat.respond(user_input)
    st.text_area("Tajinebot :", value=response, height=200, max_chars=None, key=None)


#streamlit run Chatbot.py