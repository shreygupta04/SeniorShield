//
//  ContentView.swift
//  SeniorShield
//
//  Created by Shrey Gupta on 4/10/21.
//

import SwiftUI
import Firebase

var ref: DatabaseReference!

struct ContentView: View {
    @State var name: String = ""
    var names = ["Shrey", "Atin", "Aryan", "Trishal"]
    var body: some View {
        VStack(spacing: 20) {
            HStack {
                Image(systemName: "moon.zzz.fill")
                    .font(.system(size: 30))
                Text("Good evening, Stanley.")
                    .font(.system(size: 30))
            }
            if !name.isEmpty {
                Text(names.contains(name) ? "\(name) is outside." : "An unrecognized visitor is outside.").bold()
                    .font(.system(size: 30))
                if names.contains(name) {
                    Image("shrey")
                        .resizable()
                        .cornerRadius(20)
                        .aspectRatio(contentMode: .fit)
                        .padding(50)
                    HStack {
                        Image(systemName: "checkmark.seal.fill")
                            .foregroundColor(Color.blueGreen)
                            .font(.system(size: 20))
                        Text("verified visitor")
                            .textCase(.uppercase)
                            .font(.system(size: 20))
                    }
                } else {
                    Button(action: {
                        
                    }) {
                        Text("Contact family network")
                            .padding()
                            .background(Color.blueGreen)
                            .cornerRadius(10)
                            .foregroundColor(Color.white)
                    }
                    .padding()
                    .frame(alignment: .center)
                }
            }
                
        }
//        .foregroundColor(Color.white)
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .background(Color.paleGreen)
        .edgesIgnoringSafeArea(.all)
        .foregroundColor(.white)
        .onAppear(perform: {
            ref = Database.database().reference()
            ref.child("name").observe(DataEventType.value, with: { (snapshot) in
                self.name = snapshot.value! as! String
                print(self.name)
            })
        })
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
