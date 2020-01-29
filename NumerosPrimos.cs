using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ejercicio1Plataformas
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] vec1 = new int[4000];
            generarPrimos(vec1);
            Imprimir(vec1);
        }

        public static void generarPrimos(int[] vec1)
        {
            int cont1 = 1, cont2 = 0,cont3 = 0;
            bool bandera = false;

            for (int i = 0; i < vec1.Length; i++)
            {
                cont1++;
                cont2 = 0;
                for (int j = 1; j < cont1; j++)
                {
                    if (cont1 % j == 0)
                    {
                        cont2++;
                    }
                }
                
               
              if(cont3 == 418)
                {
                    break;
                }
                else
                {
                    if (cont2 == 1)
                    {
                        vec1[i] = cont1;
                        cont3++;

                    }
            }
        }

   
        public static void Imprimir(int[] vec1)
        {
            for(int i = 0; i < vec1.Length; i++)
            {
                    if (vec1[i] != 0)
                    {
                        Console.WriteLine("El numero primo " + i  + " es " + vec1[i]);
                        Console.ReadKey();
                    }
            }
            
        }
       
    }
}
