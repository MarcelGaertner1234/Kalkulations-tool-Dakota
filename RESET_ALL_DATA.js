/**
 * DAKOTA KALKULATIONS-TOOL - KOMPLETTER DATEN-RESET
 *
 * ACHTUNG: Dieses Script löscht ALLE Daten unwiderruflich!
 * - Firestore (Cloud): lebensmittel, rezepte, menuekarten
 * - IndexedDB (lokal): DakotaKalkulationDB
 * - localStorage Flags
 *
 * ANLEITUNG:
 * 1. Öffne die Dakota App im Browser
 * 2. Öffne DevTools (F12)
 * 3. Gehe zu Console Tab
 * 4. Kopiere dieses komplette Script
 * 5. Füge es in die Console ein und drücke Enter
 * 6. Warte auf "🎉 RESET KOMPLETT!" Meldung
 * 7. Seite wird automatisch neu geladen
 */

(async function resetAllData() {
    console.log('🚨 STARTE KOMPLETTEN DATEN-RESET...\n');

    let stats = {
        firestoreLM: 0,
        firestoreRZ: 0,
        firestoreMK: 0,
        indexedDB: false,
        localStorage: false
    };

    // ===== SCHRITT 1: FIRESTORE LEEREN =====
    console.log('📍 SCHRITT 1: Firestore Cloud-Daten löschen...\n');

    if (!window.firestoreDB) {
        console.warn('⚠️ Firebase ist nicht geladen. Überspringe Firestore-Löschung.');
        console.warn('   Du musst Firestore manuell leeren über: https://console.firebase.google.com/\n');
    } else {
        try {
            const { collection, getDocs, deleteDoc, doc } = window.firebaseModules;

            // 1.1 Lebensmittel löschen
            console.log('  🗑️  Lösche Lebensmittel...');
            const lmSnapshot = await getDocs(collection(window.firestoreDB, 'lebensmittel'));
            for (const docSnapshot of lmSnapshot.docs) {
                await deleteDoc(doc(window.firestoreDB, 'lebensmittel', docSnapshot.id));
            }
            stats.firestoreLM = lmSnapshot.size;
            console.log(`  ✅ ${lmSnapshot.size} Lebensmittel aus Firestore gelöscht\n`);

            // 1.2 Rezepte löschen
            console.log('  🗑️  Lösche Rezepte...');
            const rzSnapshot = await getDocs(collection(window.firestoreDB, 'rezepte'));
            for (const docSnapshot of rzSnapshot.docs) {
                await deleteDoc(doc(window.firestoreDB, 'rezepte', docSnapshot.id));
            }
            stats.firestoreRZ = rzSnapshot.size;
            console.log(`  ✅ ${rzSnapshot.size} Rezepte aus Firestore gelöscht\n`);

            // 1.3 Menükarten löschen
            console.log('  🗑️  Lösche Menükarten...');
            const mkSnapshot = await getDocs(collection(window.firestoreDB, 'menuekarten'));
            for (const docSnapshot of mkSnapshot.docs) {
                await deleteDoc(doc(window.firestoreDB, 'menuekarten', docSnapshot.id));
            }
            stats.firestoreMK = mkSnapshot.size;
            console.log(`  ✅ ${mkSnapshot.size} Menükarten aus Firestore gelöscht\n`);

        } catch (error) {
            console.error('❌ Fehler beim Löschen von Firestore:', error);
            console.warn('   Versuche Firestore manuell zu leeren über Firebase Console\n');
        }
    }

    // ===== SCHRITT 2: INDEXEDDB LÖSCHEN =====
    console.log('📍 SCHRITT 2: IndexedDB lokale Datenbank löschen...\n');

    try {
        const deleteRequest = indexedDB.deleteDatabase('DakotaKalkulationDB');

        deleteRequest.onsuccess = () => {
            console.log('  ✅ IndexedDB "DakotaKalkulationDB" gelöscht\n');
            stats.indexedDB = true;
        };

        deleteRequest.onerror = (event) => {
            console.error('  ❌ IndexedDB Löschung fehlgeschlagen:', event);
        };

        deleteRequest.onblocked = () => {
            console.warn('  ⚠️  IndexedDB Löschung blockiert. Schließe alle anderen Tabs mit dieser App.\n');
        };

        // Warte kurz auf Completion
        await new Promise(resolve => setTimeout(resolve, 500));

    } catch (error) {
        console.error('❌ Fehler beim Löschen von IndexedDB:', error);
    }

    // ===== SCHRITT 3: LOCALSTORAGE FLAGS LÖSCHEN =====
    console.log('📍 SCHRITT 3: localStorage Flags löschen...\n');

    try {
        const flagsBefore = {
            autoImport: localStorage.getItem('dakota_auto_import_done'),
            firestoreMigrated: localStorage.getItem('firestore_migrated')
        };

        console.log('  Vor Löschung:');
        console.log(`    dakota_auto_import_done: ${flagsBefore.autoImport}`);
        console.log(`    firestore_migrated: ${flagsBefore.firestoreMigrated}\n`);

        localStorage.removeItem('dakota_auto_import_done');
        localStorage.removeItem('firestore_migrated');

        console.log('  ✅ localStorage Flags gelöscht\n');
        stats.localStorage = true;

    } catch (error) {
        console.error('❌ Fehler beim Löschen von localStorage:', error);
    }

    // ===== ZUSAMMENFASSUNG =====
    console.log('═'.repeat(60));
    console.log('📊 RESET ZUSAMMENFASSUNG\n');
    console.log(`Firestore Lebensmittel gelöscht:  ${stats.firestoreLM}`);
    console.log(`Firestore Rezepte gelöscht:       ${stats.firestoreRZ}`);
    console.log(`Firestore Menükarten gelöscht:    ${stats.firestoreMK}`);
    console.log(`IndexedDB gelöscht:                ${stats.indexedDB ? '✅' : '❌'}`);
    console.log(`localStorage gelöscht:             ${stats.localStorage ? '✅' : '❌'}`);
    console.log('═'.repeat(60));
    console.log('\n🎉 RESET KOMPLETT!\n');
    console.log('Die Seite wird in 3 Sekunden neu geladen...\n');
    console.log('Nach dem Reload:');
    console.log('  - 0 Lebensmittel, 0 Rezepte');
    console.log('  - Alle Daten gelöscht');
    console.log('  - Du kannst neu starten (JSON-Import oder manuell)');

    // ===== SCHRITT 4: AUTO-RELOAD =====
    setTimeout(() => {
        console.log('\n🔄 Lade Seite neu...');
        location.reload(true);
    }, 3000);

})();
